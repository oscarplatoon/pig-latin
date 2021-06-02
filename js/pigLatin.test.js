const pig = require('./pigLatin');

const{ test } = require ('@jest/globals')


test('Does it return a string?', () => {
  expect(typeof(pig.translate("test"))).toBe('string')

test("translates a word beginning with a vowel:", () => {
  expect((pig.translate("apple"))).toBe("appleay");


});
