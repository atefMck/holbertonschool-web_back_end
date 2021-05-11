import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignUp(firstName, lastName, fileName) {
  const stats = [];
  await signUpUser(firstName, lastName)
    .then(async (data) => {
      stats.push({
        status: 'Resolved',
        value: data,
      });
      await uploadPhoto(fileName);
    })
    .catch((err) => {
      stats.push({
        status: 'Rejected',
        value: err.toString(),
      });
    });
  return stats;
}
