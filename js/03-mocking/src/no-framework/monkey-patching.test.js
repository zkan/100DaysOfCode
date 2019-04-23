const assert = require('assert')
const thumbWar = require('../thumb-war')
const utils = require('../utils')

const originalGetWinner = utils.getWinner

// monkey patching
utils.getWinner = (p1, p2) => p1

const winner = thumbWar('Kan Ouivirach', 'Mils Burasakorn')
assert.strictEqual(winner, 'Kan Ouivirach')

utils.getWinner = originalGetWinner
