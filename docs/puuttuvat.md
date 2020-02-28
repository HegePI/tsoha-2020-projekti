# Puuttuvat ominaisuudet

1. Työn alussa oli suunnitelma, että Dungeon Masteri pystyy "aloittamaan seikkailun" tai "jatkamaan seikailua". Tämä olisi toteutettu luomalla oma peli -näkymä, joka listaisi kaikki seikkailussa paikalla olvat hahmot, joiden tietoja Dungeon Master pystyisi muokkaamaan esim. hahmon elinvoiman vähennys taistelussa tai esineen lisäys hahmolle.

2. Sovelluksessa käyttäjä ei voi luoda hahmoa siten, etteikö se liittyisi johonkin seikkailuun. Ajatus alussa oli yksi hahmo per seikkailu per käyttäjä. Jotta sovelluksessa voisi luoda hahmoja talteen, tulisi olla olemassa hahmo-seikkailu liitostaulu. Tällöin käyttäjä voi valita hahmon, jonka liittä seikkailuun sen sijaan, että loisi aina uuden hahmon.

3. Alussa oli suunnitelma, että hahmoluokkia voisi luoda uusia, jotka talletettaisiin class -tietokantatauluun. Tällöin aina kun käyttäjä loisi hahmoa, voisi hän valita jo olemassa olevista luokista tai luoda uuden luokan. Jos käyttäjä luo uuden hahmo luokan, niin se talletetaisiin, class- tietokantatuluun.