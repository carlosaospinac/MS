from fastapi import HTTPException
from sqlalchemy.orm import Session

from models import Organization, Role, User
from schemas.organization import CreateSchema, CompleteCreationSchema
from db import use_db


@use_db
def create(payload: CreateSchema, db: Session=None):

    existing_org = Organization.get_by_prefix(db, payload.prefix)
    if existing_org:
        raise HTTPException(400, 'Prefix not available')

    organization = Organization(name=payload.name, prefix=payload.prefix)
    ownerRole = Role(code=Role.CODE_OWNER)
    defaultRole = Role(code=Role.CODE_DEFAULT)
    organization.roles.append(ownerRole)
    organization.roles.append(defaultRole)

    user = User(**payload.owner.__dict__)
    user.role = ownerRole

    organization.users.append(user)

    organization.save(db)

    return organization


@use_db
def get_list(db: Session=None):

    return Organization.get_list(db)


@use_db
def get(ident, db: Session=None):
    return Organization.get(db, ident)


@use_db
def complete_creation(ident, payload: CompleteCreationSchema, db: Session=None):
    org = Organization.get(db, ident)
    if org is None:
        raise HTTPException(404, 'Organization not found')

    owner: User = org.users[0]

    org.status = Organization.STATUS_ACTIVE
    owner.status = User.STATUS_ACTIVE
    owner.password = payload.password

    org.update(db)

    return org
