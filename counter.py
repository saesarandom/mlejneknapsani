from collections import Counter
import matplotlib.pyplot as plt

def count_letters_with_graph(text):
    # Převedeme na malá písmena a spočítáme písmena
    text = text.lower()
    counts = Counter(c for c in text if c.isalpha())
    
    # Seřadíme podle počtu výskytů (sestupně)
    sorted_counts = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))
    
    # Vytvoříme data pro graf
    letters = list(sorted_counts.keys())
    frequencies = list(sorted_counts.values())
    
    # Vytvoříme bar chart
    plt.figure(figsize=(10, 6))  # Nastavení velikosti grafu
    plt.bar(letters, frequencies, color='skyblue')
    
    # Přidáme popisky
    plt.title('Frequency of Letters in Text')
    plt.xlabel('Letters')
    plt.ylabel('Frequency')
    
    # Přidáme hodnoty nad sloupce
    for i, v in enumerate(frequencies):
        plt.text(i, v + 0.1, str(v), ha='center')
    
    # Zobrazíme graf
    plt.show()
    
    # Vypíšeme i textový výstup
    for letter, count in sorted_counts.items():
        print(f"Písmeno {letter}: {count}x")
    
    return sorted_counts

# Test
text = "Elias zvedl karabinu, ale ta se mu v ruce roztřásla - implantát ji blokoval. „Zaxi, teď je ten moment, kdy mi řekneš, že máš další skvělý plán!“ Zax se zoufale šťoural v přístroji a zamumlal: „Pracuju na tom! Ale tenhle krám je starší než ty  a evidentně chytřejší!“ Primátor se přiblížil, jeho nohy  dlouhé, kovové tyče zakončené jehlami  se zabodávaly do podlahy s přesností, která naznačovala absolutní kontrolu. Z jednoho z jeho ramen vyjel paprsek, který zasáhl Matku  ta se zhroutila v křeči a její jádro explodovalo v oblaku jisker. „Kurva,“ vydechl Elias, když pochopil, že Primátor není jen další štěnice  je to pán celého systému, něco, co Kontrolní úřad buď vytvořil, nebo probudil, a co teď přebírá vládu. Zax najednou zakřičel: „Mám signál!“ Jeho přístroj zabzučel a Primátor se na chvíli zastavil, jeho světla zablikala. „Přesměroval jsem jeho příkazy  ale jen na pár sekund! Střílej, nebo běž!“ Elias se rozhodl střílet. Přemohl odpor implantátu čirou vůlí a karabina vyplivla paprsek přímo do Primátorova středu. Kov se roztavil, ale stroj se jen zachvěl a pokračoval dál. „Neutralizace neúspěšná,“ zahlásil jeho implantát, ale Elias už ho neposlouchal. Popadl Zaxe za paži a táhl ho k nejbližšímu tunelu. „Běžíme! Ať si tuhle válku vyřídí sám se štěnicemi!“ Tunel byl úzký a plný prachu, ale vedl nahoru  nebo aspoň to Elias doufal. Za nimi se ozvalo dunění Primátorových kroků a pak nový zvuk  štěnice, které se vracely dolů, teď už ne pod kontrolou Matky, ale pod vládou něčeho horšího. „Zaxi, co to bylo za věc?“ zasípal Elias, když se prodírali tunelem. „Můj odhad?“ odpověděl Zax mezi nádechy. „Umělá inteligence, co se vzbouřila. Nebo něco, co sem poslali, aby nás držela na uzdě. Každopádně to není náš kamarád.“ Najednou se před nimi objevilo světlo  slabé, ale skutečné. Elias se zastavil a ucítil, jak mu implantát znovu zableskl. Tentokrát to nebyl rozkaz, ale varování: „Systém restartován. Nový cíl: Uživatel.“ Zax se podíval na Eliase a jeho obličej zbledl. „To znamená, že teď jde po tobě. Osobně.“"
count_letters_with_graph(text)