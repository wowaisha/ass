#4.1 feladat
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


#4.2 feladat
var data = [28, 31, 44, 29]; // Observed weights

var simpleModel = function() {
    // Prior distribution based on the average weight and standard deviation
    var mu_prior = 32; // Mean from the lexicon
    var sigma_prior = 10; // Standard deviation from the lexicon
    var Prior = Gaussian({ mu: mu_prior, sigma: sigma_prior });

    // Likelihood for each observed weight
    for (var i = 0; i < data.length; i++) {
        observe(Gaussian({ mu: Prior.mu, sigma: 1 }), data[i]);
    }

    // Posterior distribution
    var Posterior = Gaussian({ mu: Prior.mu, sigma: sigma_prior });

    return {
        Prior: Prior,
        Posterior: Posterior
    };
};

var opts = { method: 'SMC', particles: 2000, rejuvSteps: 5 };

var output_1 = Infer(opts, simpleModel);

// Visualize the marginals of the posterior distribution
viz.marginals(output_1);
