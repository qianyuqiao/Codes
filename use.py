import alchemy
from alchemy import session
from alchemy import User

query=session.query(User)
print query.all()
