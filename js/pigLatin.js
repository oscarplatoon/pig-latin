// # Premise
// Pig Latin is a made-up children's language that's intended to be confusing. It obeys a few simple rules (below) but when it's spoken quickly it's really difficult for non-children (and non-native speakers) to understand.

// Rule 1: If a word begins with a vowel sound, add an "ay" sound to the end of the word.

// Rule 2: If a word begins with a consonant sound, move it to the end of the word, and then add an "ay" sound to the end of the word.

// (There are a few more rules for edge cases, and there are regional variants too, but that should be enough to understand the tests.)

// See <http://en.wikipedia.org/wiki/Pig_latin> for more details.


export function translate(word) {

  let vowels = ['a','e','i','o','u']
  let result = []

// if word starts with a vowel return 'ay' at the end
  word.split(' ').forEach(element => {
    if (vowels.incluces(element[0])) {
      result.push(element + 'ay')
    }
    else {
      for(let i = 0; i < word.length; i++) {
        if (!vowels.includes(word[i])) i++
        else if ( vowels.includes(word[i])) {
          let beggingingWord = word.slice(0,i)
          let endWord = word.slice(i) + 'ay'
          result.push(beggingingWord + endWord)
        }
      }
    }
    return result.join(' ')
  });
}
// if word starts with consonant sound, move it to the end and add 'ay'

// return result

console.log(translate('apple'))