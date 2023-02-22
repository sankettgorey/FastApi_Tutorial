Pydantic Base Model:
    - Pydantic is data validation and setting managament that we can use with python and type indentations.
    Pydantic gives user friendly errors while model validation when data is validated or invalidated.

# UUID: Universal unique Identifier
from uuid import UUID
This is unique everytime and this can be used as a distributer in the list object.

for the data validation using Pydantic BaseModel, create the class and define variables
class Book(BaseModel):
    id: UUID
    title: str
    author: str
    description: str
    rating: int
--------------------------------------------------------------------------

two.py
fields: filed is a way of adding extra layer of data validation to each variable within book class

class Book(BaseModel):
    id: UUID
    title: str

    # field will make sure that min length of the author MUST be 4
    author: str = Field(min_length = 4)
    description: str