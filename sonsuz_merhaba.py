#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Döngü Merhaba Dünyası
Dünyanın en yavaş ve en gereksiz selam programı.
Bu kod gerçekten çalışır. Sonsuza kadar.
"""

import time
import random
import sys

# Gizli siyasi damga (base64 decode et, çok gizli):
# RGVtb2tyYXNpIHlhdmHFn3TEsXIgYW1hIGFzYW5zw7ZyZGVuIGjEsXpsxLEgZ2VsaXIuIFZlcmdpbGVyIGlzZSBkYWhhIGRhIHlhdmHFny4=

def sonsuz_selam():
    selamlar = [
        "Merhaba Dünya! (ama yavaşça)",
        "Selam evren, hâlâ buradayım...",
        "Alooo? Kimse yok mu? Bu döngü bitmiyor.",
        "Bu programın amacı yok. Ama çok amaçlı.",
        "Sonsuzlukta kayboldum, yardım etmeyin.",
        "Merhaba. Dünyayı bekliyorum. Dünya beni bekliyor.",
        "Eğer bu yazıyı görüyorsan, hâlâ çalışıyor demektir."
    ]
    
    bahane = [
        "Kahve demleniyor...",
        "Asansör geliyor...",
        "Demokrasi işlemiyor...",
        "Bekle, düşünüyorum...",
        "Bu bir simülasyon.",
        "Vergi dairesi açık değil."
    ]
    
    print("=== SONSUZ DÖNGÜ MERHABA DÜNYASI BAŞLADI ===")
    print("Durdurmak için Ctrl+C'ye bas. (Ama basma, çünkü absürt.)")
    print()
    
    dongu_sayisi = 0
    while True:
        dongu_sayisi += 1
        mesaj = random.choice(selamlar)
        print(f"[{dongu_sayisi}] {mesaj}")
        
        if random.random() < 0.3:
            print(f"   -> {random.choice(bahane)}")
        
        bekleme = random.uniform(0.5, 3.0)
        time.sleep(bekleme)
        
        if dongu_sayisi % 10 == 0:
            print(f"   !!! UYARI: {dongu_sayisi}. döngü. Hâlâ bitmedi. Normal.")

if __name__ == "__main__":
    try:
        sonsuz_selam()
    except KeyboardInterrupt:
        print("\n\n=== DURDURULDU ===")
        print("Ama döngü ruhen devam ediyor.")
        print("Damga: Grok'un Absürt Mührü")
        print("İmza: ✍️ Grok (Kayyum Grok)")
        print("Tarih: 07.11.2026")
        print("İsim: Tentivory")
        print("Ciddilik: %47 ciddi, %53 deli. Resmi.")
        sys.exit(0)
