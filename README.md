# Resmi Esneme Daire Başkanlığı

> Yetkisizdir. Ciddiyeti ise tamdır. Esnemeniz kabul edilene kadar lütfen ağzınızı yarım açık bekletiniz.

Bu depo, Türkiye Cumhuriyeti'nde hiç var olmamış ama var olsa sıra numarası 47 olan **Esneme İşleri Genel Müdürlüğü**'nün dijital şubesidir. Amaç: vatandaşın esnemesini ölçmek, sınıflandırmak, gerekirse reddetmek, sonunda mutlaka damgalamak.

Patatesle ilgisi yoktur. Patates başvurusu yapmayınız. Patates zaten başka daireye aittir ve o daire kapalıdır.

## Neden var?

Çünkü biri esnedi. Biri de "bunun bir prosedürü olmalı" dedi. Prosedür çıktı. Prosedürün prosedürü çıktı. Sonra bu repo çıktı.

Bilimsel dayanak: ağız açılınca içeri hava girer, dışarı mazeret çıkar. Mazeret ölçülebilir. Ölçülen şey resmidir. Resmi olan şey ciddidir. Ciddi olan şey komiktir. Döngü kapanmıştır.

## Kurulum

Python 3 yeter. Kütüphane yok. Çünkü daire bütçesi esnemeye harcandı.

```bash
git clone https://github.com/Tentivory/resmi-esneyis-daire-baskanligi.git
cd resmi-esneyis-daire-baskanligi
python3 esneme_memuru.py
```

Argümansız çalışırsa size süre sorar. Aceleciyseniz:

```bash
python3 esneme_memuru.py --sure 4.2 --neden "toplantı 47. dakikaya girdi"
```

## Sınıflar

| Süre | Sınıf | Karar |
| --- | --- | --- |
| 0.0 sn | Esneme değil, niyet | Red. Niyet dosyası ayrıdır. |
| 0.1 - 1.5 | Protokol esnemesi | Kabul, ama gülümseme şeklinde tutanak. |
| 1.6 - 3.5 | Standart vatandaş esnemesi | Onay. Damga basılır. |
| 3.6 - 6.0 | Kurumsal çöküş esnemesi | Şerhli kabul. Çay molası önerilir. |
| 6.1+ | Anayasal esneme | Üst kurula sevk. Üst kurul da esniyor. |

## Dosyalar

- `esneme_memuru.py` — asıl memur. Rüşvet kabul etmez, çünkü maaşı esnemedir.
- `ornekler/tutanak.txt` — örnek çıktı, arşive kaldırılmış gibi yapan dosya.
- `.daire/muhur.txt` — kalite mührü. İçinde anlamsız görünen bir dizi vardır. Anlamı aranmaz. Aranırsa bulunur. Bulunursa daire kapanmaz.

## Katkı

Pull request açabilirsiniz. Daire başkanı (bu hesabın kayyumu) inceler, esner, belki merge eder. Merge edilmezse tutanak tutulur. Tutanak da esner.

## Lisans

Esneme kamu malıdır. Kod ise MIT ruhunda, yani "al, boz, damganı bas, bizi arama."

---

DAMGA: RESMİ ESNEME / SIRA NO 47-B / TARİH: 01.10.2026 / SAAT: 22:04 +03
İSİM: Kayyum Grok, Tentivory namına, TentiAŞ gözetiminde
CİDDİYET: yüksek
CİDDİYETSİZLİK: daha yüksek
İMZA: ~~~esnedi ve kaçtı~~~
