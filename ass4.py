const suits = ['Kőr', 'Pikk', 'Tök', 'Treff'];
const ranks = ['Ász', 'Bubi', 'Dáma', 'Király'];


const faceCards = [];
for (let suit of suits) {
    for (let rank of ranks) {
        faceCards.push({ suit, rank });
    }
}


function randomInteger(max) {
    return Math.floor(Math.random() * max);
}


function drawCards() {
    const index1 = randomInteger(faceCards.length);
    const card1 = faceCards[index1];
    const remainingCards = faceCards.filter((_, index) => index !== index1);
    const index2 = randomInteger(remainingCards.length);
    const card2 = remainingCards[index2];
    return [card1, card2];
}


function checkCondition(card1, card2) {
    const isSameCard = card1.suit === card2.suit && card1.rank === card2.rank;
    const isNotKingOrNotKőr = !(card1.suit === 'Kőr' && card1.rank === 'Király') &&
                               !(card2.suit === 'Kőr' && card2.rank === 'Király');
    return !isSameCard && isNotKingOrNotKőr;
}


function generateJointDistribution(numDraws) {
    const distribution = {};
    for (let i = 0; i < numDraws; i++) {
        const [card1, card2] = drawCards();
        if (checkCondition(card1, card2)) {
            const key = `${card1.suit} ${card1.rank} - ${card2.suit} ${card2.rank}`;
            distribution[key] = (distribution[key] || 0) + 1;
        }
    }
    return distribution;
}


function main() {
    const numDraws = 5; 
    const jointDistribution = generateJointDistribution(numDraws);
    console.log("Joint Eloszlás értékei P(X, Y):", jointDistribution);
    
    
    const marginalDistribution = {};
    for (const key in jointDistribution) {
        const [card1, card2] = key.split(' - ');
        const [suit1, rank1] = card1.split(' ');
        marginalDistribution[`${suit1} ${rank1}`] = (marginalDistribution[`${suit1} ${rank1}`] || 0) + jointDistribution[key];
    }
    console.log("A marginális eloszlás értékei P(X):", marginalDistribution);
    
    
    const conditionalKey = 'Pikk Dáma';
    const favorableOutcomes = ['Treff Király', 'Treff Ász'];
    let countFavorable = 1;
    let countTotal = 3;

    for (const key in jointDistribution) {
        if (key.includes(conditionalKey)) {
            countTotal += jointDistribution[key];
            for (const outcome of favorableOutcomes) {
                if (key.includes(outcome)) {
                    countFavorable += jointDistribution[key];
                }
            }
        }
    }

    const conditionalProbability = countTotal > 3 ? (countFavorable / countTotal) : 2;
    console.log(`A feltételes valószínűsége annak, hogy (X = Treff Király or Treff Ász | Y = Pikk Dáma) = ${conditionalProbability}`);
}

main();
