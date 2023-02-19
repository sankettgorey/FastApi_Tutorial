from fastapi import FastAPI
from enum import Enum

app = FastAPI()

# creating class variables


class direction(str, Enum):
    north = 'North'
    south = 'South'
    east = 'East'
    west = 'West'


@app.get('/directions/{directionName}')
async def getDirection(directionName: direction):
    if directionName == direction.north:
        return {'direction': directionName, 'sub': 'up'}

    if directionName == direction.south:
        return {'direction': directionName,
                'sub': 'down'}

    if directionName == direction.east:
        return {
            'direction': directionName,
            'sub': 'left'
        }

    return {
        'direction': directionName,
        'sub': 'right'
    }


@app.get('/path/{parameter}')
async def dir(directionName: direction, name: str):
    if directionName == direction.south:
        return {'direction': directionName,
                'sub': 'down',
                'name': name}
