export default function cleanSet(set, startString) {
  const tmp = [];
  set.forEach((element) => {
    if (startString !== '' && element.startsWith(startString)) {
      tmp.push(element.replace(startString, ''));
    }
  });
  return tmp.join('-');
}
