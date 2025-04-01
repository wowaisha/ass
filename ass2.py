Lemma problem_1 : forall A B C : Prop, A /\ (B \/ C) -> (A /\ B) \/ (A /\ C).
Proof.
intros A B C H. # ha H igaz
  destruct H as [HA HBC]. # ha A és HBC B \/ C 
  destruct HBC as [HB | HC]. # az esetszétválasztása
  - left. split; assumption. # ha a HB igaz, akkor (A /\ B) igaz = bal oldal
  - right. split; assumption. # ha HC igaz, akkor (A /\ C) igaz = jobb oldal
Qed.

Lemma problem_2 : forall A B C : Prop, ((B -> A) /\ (C -> A)) -> (B \/ C -> A).
Proof.
intros A B C H HBC. # feltesszük, hogy H és HBC igaz
  destruct H as [HBA HCA]. # szétszedjük a konjunkciót, HBA: B -> A és HCA: C -> A
  destruct HBC as [HB | HC]. # esetszétválasztás a diszjunkcióra
  - apply HBA; assumption. # ha HB igaz, akkor B -> A alapján A is igaz
  - apply HCA; assumption. # ha HC igaz, akkor C -> A alapján A is igaz
Qed.

Lemma problem_3 : forall A B : Prop, (A \/ ~A) -> ((A -> B) -> A) -> A.
Proof.
intros A B H1 H2.
destruct H1 as [HA | HNA].
  - exact HA. # ha A igaz, akkor A is igaz
  - specialize (H2 (fun _ => B)). # ha ~A igaz, negáció és implikáció
    apply H2.
    intro H. # feltételezve A igaz, ez ellentmondás
    apply HNA. exact H.
Qed.

Lemma problem_4 : forall (U : Type) (A B : U -> Prop), (exists x, A x /\ B x) -> (exists x, A x) /\ (exists x, B x).
intros U A B H.
destruct H as [x HAB].  # szétszedjük az 'exists x, A x /\ B x' kifejezést.
destruct HAB as [HA HB].  # szétszedjük az 'A x' és 'B x' -t
  split.
  - exists x. exact HA. # van egy 'x', amelyre 'A x' igaz.
  - exists x. exact HB.  # létezik egy 'x', amelyre 'B x' igaz.
Qed.
