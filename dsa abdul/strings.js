str = "jagaag";

// console.log(str.length);

function caseChanger(str) {
  let converted = str.split("");
  for (let i = 0; i < converted.length; i++) {
    if (converted[i] == converted[i].toLowerCase())
      converted[i] = converted[i].toUpperCase();
    else converted[i] = converted[i].toLowerCase();
  }
  return converted.join("");
}

function caseChanger2(str) {
  //using lexological order same as the ascii code answer for c language
  let converted = str.split("");
  for (let i = 0; i < converted.length; i++) {
    if (converted[i] >= "a") converted[i] = converted[i].toUpperCase();
    else converted[i] = converted[i].toLowerCase();
  }
  return converted.join("");
}

str2 = "wElCOme";
// console.log(caseChanger2(str2));
// console.log(caseChanger(str2));

function vowelCounter(str) {
  let vowels = 0,
    consonants = 0;
  for (let i = 0; i < str.length; i++) {
    if (str[i].toLowerCase().match(/a|e|i|o|u/) !== null) vowels++;
    //else if (str[i].toLowerCase().match()
    //finish the consonant counter
  }

  return vowels;
}
str3 = "How are you?";
//console.log(vowelCounter(str3));

function validator(str) {
  // validate if the string contains special characters
  let arr = str.split("");
  let specials = ["!", "@", "#", "$", "%", "^", "&", "?", "/"];
  for (let i = 0; i < specials.length; i++) {
    if (arr.includes(specials[i])) return "invalid string";
  }
  return "valid string";
}

// work on the validator problem with regex pattern

function reversor(str) {
  // str = str.split("").reverse().join("");
  let arr = str.split(""),
    i = 0;
  j = arr.length - 1;
  while (i < j) {
    temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
    i++;
    j--;
  }

  let ans = arr.join("");
  return ans;
}

function reversor2(str) {
  //answer with another array
  let arr = str.split(""),
    ans = [],
    n = arr.length - 1;
  for (let i = 0; i < arr.length; i++) {
    ans[i] = arr[n - i];
  }
  return ans.join("");
}

//console.log(reversor2("hello"));

function palindrome(str) {
  let rev = str.split("").reverse().join("");
  if (rev === str) return true;
  return false;
}

//console.log(palindrome("kodok"));

function dupliacates(str) {
  //duplicate founding using bitwise operations
}

function checkAnagram(str) {}
