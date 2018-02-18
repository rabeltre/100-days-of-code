log = console.log
expect = require('chai').expect
should = require('chai').should()
_= require('lodash')

const {
    alwaysTrue, 
    legitString
} = require('./index')

describe('#mocha basics', function (){
  //unit test are here man...

  it('true shoul be true', function (){
      true.should.be.true;
    });

    it('I expect true to be true', function(){
        expect(true).to.be.true;
    });
})

describe('#AlwaysTrue' , ()=>{
    it('should always return true', ()=>{
        alwaysTrue().should.be.true;
    });
    it('It expect it to always be true', ()=>{
        expect(alwaysTrue()).to.be.true;
    });
    it('should not be false', ()=>{
        alwaysTrue().should.not.be.false;
    });
})

describe('#legitString', ()=>{
    it("should detect 'cow' as a legit string", ()=>{
        legitString('cow').should.be.true;
    })
    it("undefined should not be true", ()=>{
        legitString(undefined).should.be.false;
    })
})