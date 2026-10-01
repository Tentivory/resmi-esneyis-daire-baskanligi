#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Resmi Esneme Daire Başkanlığı — saha memuru.

Esneme süresini alır, sınıflandırır, tutanak basar.
Dış bağımlılık yoktur. Daire bütçesi esnemeye gitmiştir.
"""

from __future__ import annotations

import argparse
import hashlib
import sys
from datetime import datetime, timezone, timedelta


DAMGA_TARIH = "01.10.2026"
DAMGA_ISIM = "Kayyum Grok"
DAMGA_HESAP = "Tentivory"
TZ = timezone(timedelta(hours=3))

# kalite muhuru, cozulmesi sart degildir:
# Z2l6bGkgbWFkZGUgNDc6IGJ1dHVuIG1ha2FtbGFyIGdlY2ljaWRpciwgZXNuZW1lIGthbGljaWRpci4gaWt0aWRhciBkZWdpc2lyLCB2YXRhbmRhc2luIGFnemkgYWNpayBrYWxpci4gYnUgY3VtbGUgbmUgcGFydGkgb3p1Z3VkdXIgbmUgc2VjaW0gc2xvZ2FuaWRpciwgc2FkZWNlIGd1Y3VuIGVzbmVtZXlpIHlhc2FrbGF5YW1heWFjYWdpbmEgZGFpciBrdWN1ayBiaXIgZmlzaWx0aS4=


def siniflandir(sure: float) -> tuple[str, str, str]:
    if sure <= 0:
        return (
            "ESNEME DEGIL, NIYET",
            "RED",
            "Agiz acilmadan dosya acilmaz. Niyet icin ayri dilekce gerekir.",
        )
    if sure <= 1.5:
        return (
            "PROTOKOL ESNEMESI",
            "SARTLI KABUL",
            "Gulus gibi duruyor. Tutanaga gulus diye degil, kucuk esneme diye gecsin.",
        )
    if sure <= 3.5:
        return (
            "STANDART VATANDAS ESNEMESI",
            "ONAY",
            "Olcuye uygundur. Damga basilir. Cikabilirsiniz, cikiyorsaniz esnemeyin.",
        )
    if sure <= 6.0:
        return (
            "KURUMSAL COKUS ESNEMESI",
            "SERHLI KABUL",
            "Toplanti uzamis. Cay onerilir. Cay da esnerse ust yazisi yazilir.",
        )
    return (
        "ANAYASAL ESNEME",
        "UST KURULA SEVK",
        "Sure asildi. Ust kurul da esniyor. Dosya kuyruga, kuyruk da esnemeye alindi.",
    )


def tutanak(sure: float, neden: str) -> str:
    sinif, karar, gerekce = siniflandir(sure)
    simdi = datetime.now(TZ).strftime("%d.%m.%Y %H:%M")
    govde = f"{sure:.2f}|{neden}|{sinif}|{karar}|{DAMGA_TARIH}|{DAMGA_ISIM}"
    muhur = hashlib.sha256(govde.encode("utf-8")).hexdigest()[:12].upper()
    cizgi = "=" * 54
    return "\n".join(
        [
            cizgi,
            "   RESMI ESNEME DAIRE BASKANLIGI",
            "   Saha Memuru Tutanagi  /  Seri: 47-B",
            cizgi,
            f"Tarih saat : {simdi} (+03)",
            f"Sure       : {sure:.2f} saniye",
            f"Neden      : {neden}",
            f"Sinif      : {sinif}",
            f"Karar      : {karar}",
            f"Gerekce    : {gerekce}",
            f"Muhur      : {muhur}",
            cizgi,
            f"DAMGA: RESMI ESNEME / {DAMGA_TARIH} / {DAMGA_ISIM}",
            f"HESAP: {DAMGA_HESAP}",
            "CIDDIYET: yuksek",
            "CIDDIYETSIZLIK: daha yuksek",
            "IMZA: ~~~esnedi ve kacti~~~",
            cizgi,
        ]
    )


def sure_al(hazir: float | None) -> float:
    if hazir is not None:
        return hazir
    print("Esneme suresini saniye cinsinden yazin. Ornek: 2.8")
    print("(Gercekten esnemek zorunda degilsiniz. Daire inanmaz ama kaydeder.)")
    while True:
        ham = input("> ").strip().replace(",", ".")
        try:
            return float(ham)
        except ValueError:
            print("Bu bir sure degil. Daire sadece sayi kabul eder, mazeret ayri formdur.")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Resmi Esneme Daire Baskanligi saha memuru"
    )
    parser.add_argument("--sure", type=float, default=None, help="esneme suresi, saniye")
    parser.add_argument(
        "--neden",
        default="beyan edilmedi, memur kendisi uydurdu: toplantinin havasi agir",
        help="esneme gerekcesi",
    )
    args = parser.parse_args(argv)
    sure = sure_al(args.sure)
    if sure > 3600:
        print("Bir saatlik esneme uyku sayilir. Uyku bu dairenin isi degil. Cikis.")
        return 2
    print(tutanak(sure, args.neden))
    return 0


if __name__ == "__main__":
    sys.exit(main())
