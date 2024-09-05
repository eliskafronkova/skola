# skola
https://xeon.spskladno.cz/~holecek/Predmet_Programovani/

<ol>
		<li>
			Projekt je (od druhého ročníku) uložen na Gitu.
		</li>
		<li>Webová prezentace projektu
			<ol>
				<li>Stručný popis programu, jeho funkce, ukázky použití</li>
				<li>Seznam použitých algoritmů (včetně pseudokódu/vývojového diagramu) a knihoven</li>
				<li>Seznam autorů</li>
				<li>Odkaz na Git pro stažení.</li>
				<li>Možnost přihlášení uživatele + různý obsah pro přihlášeného/nepřihlášeného uživatele.</li>
				<li>Zobrazení databázových dat (výsledky programu, žebříček hráčů, seznam registrovaných uživatelů, a pod.)</li>
				<li>Po přihlášení na web jako admin lze mazat data z databáze.</li>
			</ol>
		</li>
		<li>Aplikace v Pythonu
			<ol>
				<li>Grafické rozhraní - např. v PyQt</li>
				<li>Grafické zobrazení - např. Pygame či knihovna pro zobrazení grafů a jejich zpracování a pod.</li>
				<li>Ukládá a načítá data z/do databáze - výsledky hry/výpočtu, záznamy o použití a pod. </li>
				<li>Ukládá a načítá data z/do souboru - např. uživatelské nastavení, poslední použité hodnoty a pod.</li>
				<li>Dokumentace kódu dle konvencí jazyka - minimálně dokumentace funkcí a tříd</li>
			</ol>
		</li>
		<li>Databáze
			<ol>
				<li>K databázi je zakreslen ER-diagram</li>
				<li>Využívá vztahy typu 1:N i M:N (tedy i JOIN při čtení dat)</li>
				<li>Má vytvořené skripty pro tvorbu tabulek (CREATE), vložení několika vzorových dat (INSERT) do každé tabulky (např. 3 záznamy do každé tabulky) a získání vzorových dat z tabulek (SELECT, JOIN) včetně filtrování, řazení, seskupování a vyhledávání</li>
				<li>Využívá atributy (datový typ, UNIQUE, NOT NULL, AUTO_INCREMENT, PK, FK, DEFAULT)</li>
				<li>Databáze je normalizovaná minimálně po <a href="https://cs.wikipedia.org/wiki/Boyceho%E2%80%93Coddova_norm%C3%A1ln%C3%AD_forma">Boyceho-Coddovu normu </a> viz také <a href="https://cs.wikipedia.org/wiki/Normalizace_datab%C3%A1ze">Normalizace databáze</a></li>
				<li>S databází komunikuje přes webové rozhraní (připravené dotazy), vlastní webové stránky i přes Python</li>
			</ol>
		</li>
	</ol>
