// Example of dynamic leaderboard update
const leaderboard = document.querySelector('.leaderboard ul');

// This could be fetched from a database or API
const leaderboardData = [
    { name: 'John Doe', waterSaved: 150 },
    { name: 'Jane Smith', waterSaved: 140 },
    { name: 'Alex Johnson', waterSaved: 130 },
];

leaderboard.innerHTML = leaderboardData.map(entry => `<li>${entry.name} - ${entry.waterSaved} liters saved</li>`).join('');
