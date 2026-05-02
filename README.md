# Laboratorijska vježba — Sprječavanje uvođenja sigurnosnih ranjivosti automatiziranom statičkom analizom koda u CI/CD cjevovodu

Laboratorijska vježba iz kolegija **Sigurnost operacijskih sustava i aplikacija** na **Fakultetu elektrotehnike i računarstva (FER), Sveučilište u Zagrebu**.

## O vježbi

Vježba demonstrira kako se statička analiza koda (SAST) može integrirati u automatizirani CI/CD cjevovod kako bi se sigurnosne ranjivosti otkrile prije nego što kod dospije u produkcijsko okruženje.

Na primjeru izmišljene tvrtke **DataVault d.o.o.** i njezine interne Python aplikacije za upravljanje korisničkim računima, pokazano je kako naizgled bezazlene programerske odluke — poput hardkodiranja credentials ili korištenja zastarjelog algoritma za hashiranje lozinki — predstavljaju ozbiljne sigurnosne propuste.

## Što ovaj repozitorij sadrži

- `app.py` — interna aplikacija tvrtke DataVault s namjerno ugrađenim sigurnosnim ranjivostima
- `.github/workflows/sast.yml` — GitHub Actions workflow koji automatski pokreće Bandit SAST alat pri svakom guranju koda

## Kako funkcionira

Pri svakom `git push`, GitHub Actions automatski pokreće **Bandit** — alat za statičku analizu Python koda. Ako Bandit pronađe ranjivost visoke ozbiljnosti, pipeline se prekida i izgradnja je označena kao neuspješna. Nakon ispravka ranjivosti, pipeline uspješno prolazi.

Povijest commitova ovog repozitorija prikazuje cijeli proces — od inicijalne nesigurne implementacije do ispravljene verzije koda.

## Autor

Eni Magdalena Oreč — FER, Zagreb, 2026.