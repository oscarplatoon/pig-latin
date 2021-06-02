const pig = require('./pigLatin');

const{ test } = require ('@jest/globals')


test('Does it return a string?', () => {
  expect(typeof(pig.translate("test"))).toBe('string')
});

test("translates a word beginning with a vowel:", () => {
  expect((pig.translate("apple"))).toBe("appleay");
});

test("translates a word beginning with a consonant:", () => {
  expect(pig.translate("banana")).toBe("ananabay")
});

test("translates a word beginning with two consonants:", () => {
  expect(pig.translate("cherry")).toBe("errychay")
})

test("translates two words:", () => {
  expect(pig.translate("eat pie")).toBe("eatay iepay")
})

test("translates a word beginning with three consonants:", () => {
  expect(pig.translate("three")).toBe("eethray")
});

test("counts 'sch' as a single phoneme:", () => {
  expect(pig.translate("school")).toBe("oolschay")
});

test("counts 'qu' as a single phoneme:", () => {
  expect(pig.translate("quiet")).toBe("ietquay")
}); 