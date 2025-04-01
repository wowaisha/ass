import random

def kartya():
    while True:
        szin1 = random.randint(1, 4)  # szín
        figura1 = random.randint(1, 4)  #figura
        szin2 = random.randint(1, 4)  #2.szín
        figura2 = random.randint(1, 4)  #2.figura
        
        if not (szin1 == szin2 and figura1 == figura2) and \   #feltételeket ellenőrzése
           (szin1 != 1 or figura2 != 1) and \
           (szin2 != 1 or figura1 != 1):
            break

    return (szin1, figura1), (szin2, figura2)

for _ in range(10):
    huzas1, huzas2 = kartya()
    print(huzas1, huzas2));
    
// Kártyák színei és figurái
const szinek = ['Kőr', 'Pikk', 'Tök', 'Treff'];
const figurak = ['Ász', 'Bubi', 'Dáma', 'Király'];

// Kártyák generálása
function generálKártyák() {
    return szinek.flatMap(szin => 
        figurak.map(figura => ({ szin, figura }))
    );
}

// Két lap húzása
function huzas(kártyák) {
    const index1 = Math.floor(Math.random() * kártyák.length);
    const lap1 = kártyák[index1];
    const kártyákMaradtak = kártyák.filter((_, index) => index !== index1);
    const index2 = Math.floor(Math.random() * kártyákMaradtak.length);
    const lap2 = kártyákMaradtak[index2];
    return [lap1, lap2];
}

// Ellenőrizzük az A eseményt
function ellenorizA(lap1, lap2) {
    const nemKőr = lap1.szin !== 'Kőr' || lap2.szin !== 'Kőr';
    const nemKirály = lap1.figura !== 'Király' || lap2.figura !== 'Király';
    return nemKőr && nemKirály;
}

// Fő program
function main() {
    const kártyák = generálKártyák();
    const eloszlas = [];

    // Kihúzunk 1000 pár lapot, hogy statisztikát készítsünk
    for (let i = 0; i < 1000; i++) {
        const [lap1, lap2] = huzas(kártyák);
        if (ellenorizA(lap1, lap2)) {
            eloszlas.push([lap1, lap2]);
        }
    }

    // Kiírjuk az eloszlást
    console.log("Érvényes húzások:");
    eloszlas.forEach(pair => {
        console.log(`${pair[0].szin} ${pair[0].figura} - ${pair[1].szin} ${pair[1].figura}`);
    });
}

// Futás
main();
