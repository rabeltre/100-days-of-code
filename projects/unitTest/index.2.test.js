const log = console.log
const _ = require('lodash')
const should = require('chai').should()

const {
    getPerson,
    Person
} = require('./index.2')

describe("#index initial conditions", ()=>{
    it('initial person is an object', ()=>{
        const person = getPerson()
        _.isObject(person).should.be.true;
    })

    it('armorBonus by default is 0 wearing leatherArmor', ()=>{
        const person = getPerson()
        person.armorBonus.should.equal(0)
    })
})


describe('#Person', ()=>{
    describe("#rollDice", ()=>{
        /*
        it("prints out Person", ()=>{
            log("Person:", Person.rollDice)
        })
        */

        it.only("should return a finite number(not Nan nor Infinity",()=>{
            const number = Person.rollDice(4, 20);
            _.isFinite(number).should.be.true;
            log("Number: " + number);
        })
    })
})