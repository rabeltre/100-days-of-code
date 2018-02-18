log = console.log
expect = require('chai').expect
should = require('chai').should()
_= require('lodash')


describe('#mocha basics', function (){
  //unit test are here man...

  it('true shoul be true', function (){
      true.should.be.true;
    });

    it('I expect true to be true', function(){
        expect(true).to.be.true;
    });
})