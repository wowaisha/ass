intros A B C H. # ha H igaz
  destruct H as [HA HBC]. # ha A és HBC B \/ C 
  destruct HBC as [HB | HC]. # az esetszétválasztása
  - left. split; assumption. # ha a HB igaz, akkor (A /\ B) igaz = bal oldal
  - right. split; assumption. # ha HC igaz, akkor (A /\ C) igaz = jobb oldal
Qed.


intros A B C H HBC. # feltesszük, hogy H és HBC igaz
  destruct H as [HBA HCA]. # szétszedjük a konjunkciót, HBA: B -> A és HCA: C -> A
  destruct HBC as [HB | HC]. # esetszétválasztás a diszjunkcióra
  - apply HBA; assumption. # ha HB igaz, akkor B -> A alapján A is igaz
  - apply HCA; assumption. # ha HC igaz, akkor C -> A alapján A is igaz
Qed.
