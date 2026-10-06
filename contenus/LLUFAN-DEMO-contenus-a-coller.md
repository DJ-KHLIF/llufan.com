# LLUFAN — les contenus à coller dans Shopify

Ce fichier évite de recopier quoi que ce soit à la main. Pour chaque
ressource : le texte **français** (à coller quand vous créez la ressource
dans Shopify) et le texte **arabe** (à coller ensuite dans
« Traduire et adapter »).

Trois façons de coller un corps de page :

1. dans l'éditeur de page, cliquez sur le bouton `</>` (afficher le code HTML),
   collez, puis revenez à la vue normale ;
2. ou dans « Traduire et adapter » → la ressource → le champ concerné ;
3. ou dans l'export des traductions, colonne `Translated content`.

> Les textes sont ceux de la **démonstration** : remplacez-les par les vôtres
> quand vous voudrez, la structure reste la même.

---

## 1. Les 10 pages

Boutique en ligne → **Pages** → Ajouter une page. Le « handle » indiqué est
l'adresse de la page : `llufan.com/pages/` + le handle.

### 1.1 — La marque

* handle : `la-marque` → adresse `/pages/la-marque`

**Titre (français)** — à coller dans « Titre » :

```text
La marque
```
**Corps (français)** — à coller dans le corps de page (bouton `</>` pour le HTML) :

```html
<p class="eyebrow">La marque</p>
<h2>Une marque algérienne, dédiée au confort de la maman et du bébé</h2>
<p>LLUFAN est née d'un constat simple : en Algérie, les mamans cherchent des produits doux, bien pensés, et un interlocuteur qui répond vraiment. Nous imaginons des produits pour la grossesse, l'allaitement et les premiers mois de bébé, avec une attention particulière portée au confort et à la simplicité au quotidien.</p><p><em>Texte de démonstration : cette page sera remplacée par l'histoire, les valeurs et la fabrication telles que LLUFAN souhaite les raconter.</em></p>
<h3>Des produits pensés ici</h3>
<p>Chaque produit part d'un besoin réel du quotidien, avec un principe : faire simple et solide.</p>
<h3>Le confort avant tout</h3>
<p>Des formes qui accompagnent le corps, des matières douces sur la peau de bébé.</p>
<h3>Choisi pour durer</h3>
<p>Des matières et des finitions pensées pour être utilisées longtemps.</p>
<h3>Un contact humain</h3>
<p>Une équipe joignable sur WhatsApp et par e-mail, avant comme après votre commande.</p>
<p><a href="/pages/contact">Nous écrire</a></p>
<p><a href="collections/all">Voir tous nos produits</a></p>
```
**Titre (arabe)** — dans « Traduire et adapter » :

```text
العلامة
```
**Corps (arabe)** :

```html
<p class="eyebrow">العلامة</p>
<h2>علامة جزائرية مخصّصة لراحة الأم والطفل</h2>
<p>وُلدت LLUFAN من ملاحظة بسيطة: في الجزائر، تبحث الأمهات عن منتجات ناعمة ومدروسة، وعن جهة تردّ عليهنّ فعلًا. نصمّم منتجات للحمل والإرضاع والأشهر الأولى من حياة الطفل، بعناية خاصة بالراحة والبساطة في اليومي.</p><p><em>نص تجريبي: ستُستبدل هذه الصفحة بحكاية العلامة وقيمها وطريقة التصنيع كما تريد LLUFAN أن ترويها.</em></p>
<h3>منتجات مدروسة هنا</h3>
<p>كل منتج يبدأ من حاجة حقيقية في اليومي، بمبدأ واحد: البساطة والمتانة.</p>
<h3>الراحة قبل كل شيء</h3>
<p>أشكال تواكب الجسم، وأقمشة ناعمة على بشرة الطفل.</p>
<h3>اختيار يدوم</h3>
<p>أقمشة ولمسات نهائية مصنوعة لتُستعمل طويلًا.</p>
<h3>تواصل إنساني</h3>
<p>فريق يمكن الوصول إليه عبر واتساب والبريد، قبل الطلب وبعده.</p>
<p><a href="collections/all">تصفّحي كل المنتجات</a></p>
```

### 1.2 — Livraison

* handle : `livraison` → adresse `/pages/livraison`

**Titre (français)** — à coller dans « Titre » :

```text
Livraison
```
**Corps (français)** — à coller dans le corps de page (bouton `</>` pour le HTML) :

```html
<p class="eyebrow">Aide</p>
<h2>Livraison partout en Algérie</h2>
<p>Nous livrons dans les 69 wilayas, à domicile ou en stop-desk. Les frais sont calculés selon votre wilaya et le mode choisi, et s'affichent automatiquement dans le formulaire de commande.</p>
<h3>Zones desservies</h3>
<p>Les 69 wilayas d'Algérie, à domicile ou en stop-desk.</p><p><em>Tarifs de démonstration : ils seront remplacés par les tarifs transporteur réels.</em></p>
<h3>Frais de livraison</h3>
<p>Le tarif dépend de la wilaya et du mode de livraison. Il apparaît dès que vous choisissez votre wilaya et votre commune dans le formulaire de commande.</p>
<p><a href="collections/all">Commander</a></p>
<h3>Paiement à la livraison</h3>
<p>Vous payez en espèces à la réception du colis, une fois la commande livrée.</p>
<h3>Suivi de la commande</h3>
<p>Pour connaître l'état de votre commande, contactez-nous sur WhatsApp.</p>
<p><em>Délais indicatifs de démonstration : 2 à 5 jours ouvrés selon la wilaya (à confirmer selon le transporteur).</em></p>
<p><a href="/pages/faq">Questions fréquentes</a></p>
```
**Titre (arabe)** — dans « Traduire et adapter » :

```text
التوصيل
```
**Corps (arabe)** :

```html
<p class="eyebrow">المساعدة</p>
<h2>التوصيل إلى كل الجزائر</h2>
<p>نوصّل إلى الولايات الـ 69، إلى المنزل أو إلى مكتب الاستلام. تُحسب التكاليف حسب ولايتك ونوع التوصيل، وتظهر تلقائيًا في نموذج الطلب.</p>
<h3>المناطق المغطاة</h3>
<p>الولايات الـ 69، إلى المنزل أو إلى مكتب الاستلام. <em>تكاليف تجريبية: ستُستبدل بأسعار شركة التوصيل الحقيقية.</em></p>
<h3>مصاريف التوصيل</h3>
<p>السعر يتوقف على الولاية ونوع التوصيل، ويظهر بمجرد اختيار الولاية والبلدية في نموذج الطلب.</p>
<h3>الدفع عند الاستلام</h3>
<p>تدفعين نقدًا عند استلام الطرد، بعد وصول الطلب.</p>
<h3>متابعة الطلب</h3>
<p>لمعرفة حالة طلبك، راسلينا على واتساب.</p>
<p><em>مدد إرشادية تجريبية: من 2 إلى 5 أيام عمل حسب الولاية (تُؤكَّد حسب شركة التوصيل).</em></p>
<p><a href="/pages/faq">الأسئلة الشائعة</a></p>
```

### 1.3 — Paiement

* handle : `paiement` → adresse `/pages/paiement`

**Titre (français)** — à coller dans « Titre » :

```text
Paiement
```
**Corps (français)** — à coller dans le corps de page (bouton `</>` pour le HTML) :

```html
<p class="eyebrow">Aide</p>
<h2>Paiement à la livraison</h2>
<p>Aucune carte bancaire n'est demandée sur le site : vous commandez, nous vous rappelons, et vous payez en espèces quand le colis vous est remis.</p>
<h3>Aucun paiement en ligne</h3>
<p>Le site ne demande ni carte bancaire ni virement. La commande est confirmée par téléphone ou par WhatsApp.</p>
<h3>Commande vérifiée</h3>
<p>Avant l'expédition, nous vérifions le récapitulatif, l'adresse et le numéro de téléphone.</p>
<h3>Vous payez à la réception</h3>
<p>Le montant est réglé en espèces au livreur, au moment de la remise du colis.</p>
<h3>Confirmation par WhatsApp</h3>
<p>Notre équipe vous contacte pour confirmer la wilaya, la commune et le mode de livraison.</p>
<p><a href="/pages/faq">Questions fréquentes</a></p>
```
**Titre (arabe)** — dans « Traduire et adapter » :

```text
الدفع
```
**Corps (arabe)** :

```html
<p class="eyebrow">المساعدة</p>
<h2>الدفع عند الاستلام</h2>
<p>لا نطلب أي بطاقة بنكية على الموقع: تطلبين، نتّصل بك، وتدفعين نقدًا عند تسليم الطرد.</p>
<h3>بدون دفع عبر الإنترنت</h3>
<p>الموقع لا يطلب بطاقة بنكية ولا تحويلًا. يُؤكَّد الطلب هاتفيًا أو عبر واتساب.</p>
<h3>طلب مُتحقَّق منه</h3>
<p>قبل الإرسال، نتحقق من ملخّص الطلب والعنوان ورقم الهاتف.</p>
<h3>الدفع عند التسليم</h3>
<p>يُدفع المبلغ نقدًا لعامل التوصيل، لحظة تسليم الطرد.</p>
<h3>تأكيد عبر واتساب</h3>
<p>يتواصل معك فريقنا لتأكيد الولاية والبلدية ونوع التوصيل.</p>
<p><a href="/pages/faq">الأسئلة الشائعة</a></p>
```

### 1.4 — Échanges et retours

* handle : `politique-de-retour` → adresse `/pages/politique-de-retour`

**Titre (français)** — à coller dans « Titre » :

```text
Échanges et retours
```
**Corps (français)** — à coller dans le corps de page (bouton `</>` pour le HTML) :

```html
<p class="eyebrow">Aide</p>
<h2>Échanges et retours</h2>
<p>Un article ne convient pas ? Voici comment faire, étape par étape.</p><p><em>Gabarit de démonstration : les conditions définitives seront fixées par LLUFAN.</em></p>
<h3>1. Nous contacter</h3>
<p>Écrivez-nous sur WhatsApp ou par e-mail en précisant votre numéro de commande et le produit concerné.</p>
<p><a href="/pages/contact">Page contact</a></p>
<h3>2. Délai</h3>
<p>La demande est à faire sous 7 jours après la réception du colis. <em>(Durée de démonstration, à valider.)</em></p>
<h3>3. État du produit</h3>
<p>L'article doit être non utilisé et dans son emballage d'origine.</p>
<h3>4. Frais de retour</h3>
<p><em>Emplacement à compléter : qui prend en charge les frais de retour (à décider par LLUFAN).</em></p>
<p><em>Page de démonstration. Remplacer par la politique de retour validée par LLUFAN.</em></p>
<p><a href="/pages/contact">Nous contacter</a></p>
```
**Titre (arabe)** — dans « Traduire et adapter » :

```text
التبديل والإرجاع
```
**Corps (arabe)** :

```html
<p class="eyebrow">المساعدة</p>
<h2>التبديل والإرجاع</h2>
<p>لم يناسبك منتج؟ إليك الطريقة خطوة بخطوة. <em>نموذج تجريبي: الشروط النهائية تُحدّدها LLUFAN.</em></p>
<h3>1. تواصلي معنا</h3>
<p>راسلينا على واتساب أو بالبريد مع رقم الطلب والمنتج المعني.</p>
<h3>2. المدّة</h3>
<p>يُقدَّم الطلب في غضون 7 أيام من الاستلام. <em>(مدّة تجريبية، في انتظار التأكيد.)</em></p>
<h3>3. حالة المنتج</h3>
<p>يجب أن يكون المنتج غير مستعمل وفي غلافه الأصلي.</p>
<h3>4. مصاريف الإرجاع</h3>
<p><em>مكان للاستكمال: من يتحمّل مصاريف الإرجاع (قرار يخصّ LLUFAN).</em></p>
<p><em>صفحة تجريبية. تُستبدل بسياسة الإرجاع المعتمدة من LLUFAN.</em></p>
<p><a href="/pages/contact">اتصلي بنا</a></p>
```

### 1.5 — Mentions légales

* handle : `mentions-legales` → adresse `/pages/mentions-legales`

**Titre (français)** — à coller dans « Titre » :

```text
Mentions légales
```
**Corps (français)** — à coller dans le corps de page (bouton `</>` pour le HTML) :

```html
<p class="eyebrow">Informations</p>
<h2>Mentions légales</h2>
<p><em>Page de démonstration : complétez les informations ci-dessous avant la mise en ligne.</em></p>
<h3>Éditeur du site</h3>
<p>LLUFAN — <em>[raison sociale, adresse et registre de commerce à compléter]</em>.</p>
<h3>Contact</h3>
<p>Nos coordonnées (WhatsApp et e-mail) sont indiquées dans le pied de page et sur la page Contact.</p>
<p><a href="/pages/contact">Page contact</a></p>
<h3>Hébergement</h3>
<p><em>[Nom et adresse de l'hébergeur à compléter]</em>.</p>
<h3>Propriété intellectuelle</h3>
<p><em>[Mentions relatives aux contenus, aux photos et à la marque à compléter]</em>.</p>
<p><em>Ce gabarit ne remplace pas un texte juridique validé.</em></p>
```
**Titre (arabe)** — dans « Traduire et adapter » :

```text
المعلومات القانونية
```
**Corps (arabe)** :

```html
<p class="eyebrow">معلومات</p>
<h2>المعلومات القانونية</h2>
<p><em>صفحة تجريبية: استكملي المعلومات أدناه قبل النشر.</em></p>
<h3>ناشر الموقع</h3>
<p>LLUFAN — [الاسم القانوني والعنوان والسجل التجاري للاستكمال].</p>
<h3>الاتصال</h3>
<p>بيانات التواصل (واتساب والبريد) موجودة في تذييل الصفحة وفي صفحة «اتصلي بنا».</p>
<h3>الاستضافة</h3>
<p>[اسم وعنوان المستضيف للاستكمال].</p>
<h3>الملكية الفكرية</h3>
<p>[بيانات المحتويات والصور والعلامة للاستكمال].</p>
<p><em>هذا النموذج لا يغني عن نصّ قانوني معتمد.</em></p>
```

### 1.6 — Conditions générales de vente

* handle : `cgv` → adresse `/pages/cgv`

**Titre (français)** — à coller dans « Titre » :

```text
Conditions générales de vente
```
**Corps (français)** — à coller dans le corps de page (bouton `</>` pour le HTML) :

```html
<p class="eyebrow">Informations</p>
<h2>Conditions générales de vente</h2>
<p><em>Gabarit de démonstration : ce texte présente la structure attendue et doit être validé avant la mise en ligne.</em></p>
<h3>1. Objet</h3>
<p><em>[Objet des conditions de vente et champ d'application à compléter.]</em></p>
<h3>2. Prix et devise</h3>
<p>Tous les prix sont affichés en dinars algériens (DZD), frais de livraison en sus selon la wilaya.</p>
<h3>3. Commande et paiement</h3>
<p>La commande se fait sur le site, sans paiement en ligne : le règlement se fait en espèces à la livraison (COD).</p>
<p><a href="/pages/paiement">Pages paiement</a></p>
<h3>4. Livraison</h3>
<p>Livraison dans les 69 wilayas, à domicile ou en stop-desk. <em>[Délais et transporteurs à compléter.]</em></p>
<p><a href="/pages/livraison">Page livraison</a></p>
<h3>5. Échanges et retours</h3>
<p><em>[Conditions d'échange et de retour à compléter.]</em></p>
<p><a href="/pages/politique-de-retour">Échanges et retours</a></p>
<h3>6. Service client</h3>
<p>Notre service client répond sur WhatsApp et par e-mail, avant et après la commande.</p>
<p><a href="/pages/contact">Page contact</a></p>
<p><em>Gabarit de démonstration, sans valeur juridique.</em></p>
```
**Titre (arabe)** — dans « Traduire et adapter » :

```text
شروط البيع العامة
```
**Corps (arabe)** :

```html
<p class="eyebrow">معلومات</p>
<h2>شروط البيع العامة</h2>
<p><em>نموذج تجريبي: يعرض هذا النص البنية المتوقعة، ويجب اعتماده قبل النشر.</em></p>
<h3>1. الموضوع</h3>
<p>[موضوع شروط البيع ومجال تطبيقها للاستكمال.]</p>
<h3>2. الأسعار والعملة</h3>
<p>كل الأسعار بالدينار الجزائري (دج)، ومصاريف التوصيل تُضاف حسب الولاية.</p>
<h3>3. الطلب والدفع</h3>
<p>يُقدَّم الطلب على الموقع، بدون دفع عبر الإنترنت: يُدفع نقدًا عند الاستلام.</p>
<h3>4. التوصيل</h3>
<p>التوصيل إلى الولايات الـ 69، إلى المنزل أو إلى مكتب الاستلام. [المدد وشركات التوصيل للاستكمال.]</p>
<h3>5. التبديل والإرجاع</h3>
<p>[شروط التبديل والإرجاع للاستكمال.]</p>
<h3>6. خدمة العملاء</h3>
<p>يجيبنا فريقنا على واتساب وبالبريد، قبل الطلب وبعده.</p>
<p><em>نموذج تجريبي، بدون قيمة قانونية.</em></p>
```

### 1.7 — Politique de confidentialité

* handle : `confidentialite` → adresse `/pages/confidentialite`

**Titre (français)** — à coller dans « Titre » :

```text
Politique de confidentialité
```
**Corps (français)** — à coller dans le corps de page (bouton `</>` pour le HTML) :

```html
<p class="eyebrow">Informations</p>
<h2>Politique de confidentialité</h2>
<p><em>Gabarit de démonstration : à compléter selon les traitements réellement effectués.</em></p>
<h3>1. Données collectées</h3>
<p>Les informations saisies dans le formulaire de commande : nom, numéro de téléphone, wilaya, commune, mode de livraison, contenu du panier.</p>
<h3>2. Utilisation</h3>
<p>Ces données servent uniquement à traiter la commande, organiser la livraison et assurer le service client.</p>
<h3>3. Conservation</h3>
<p><em>[Durée de conservation à définir.]</em></p>
<h3>4. Destinataires</h3>
<p>Les informations strictement nécessaires sont transmises au transporteur chargé de la livraison.</p>
<h3>5. Vos droits</h3>
<p>Vous pouvez demander l'accès, la rectification ou la suppression de vos données en nous contactant.</p>
<p><a href="/pages/contact">Page contact</a></p>
<p><em>Gabarit de démonstration, sans valeur juridique.</em></p>
```
**Titre (arabe)** — dans « Traduire et adapter » :

```text
سياسة الخصوصية
```
**Corps (arabe)** :

```html
<p class="eyebrow">معلومات</p>
<h2>سياسة الخصوصية</h2>
<p><em>نموذج تجريبي: يُستكمل حسب المعالجات الفعلية للبيانات.</em></p>
<h3>1. البيانات المجمَّعة</h3>
<p>المعلومات المُدخلة في نموذج الطلب: الاسم، رقم الهاتف، الولاية، البلدية، نوع التوصيل، ومحتوى السلة.</p>
<h3>2. الاستعمال</h3>
<p>تُستعمل هذه البيانات فقط لمعالجة الطلب وتنظيم التوصيل وضمان خدمة العملاء.</p>
<h3>3. مدّة الحفظ</h3>
<p>[مدّة الحفظ للاستكمال.]</p>
<h3>4. الجهات المستلمة</h3>
<p>تُنقل المعلومات الضرورية فقط إلى شركة التوصيل المكلّفة بتسليم الطلب.</p>
<h3>5. حقوقك</h3>
<p>يمكنك طلب الوصول إلى بياناتك أو تصحيحها أو حذفها بمراسلتنا.</p>
<p><em>نموذج تجريبي، بدون قيمة قانونية.</em></p>
```

### 1.8 — Questions fréquentes

* handle : `faq` → adresse `/pages/faq`

**Titre (français)** — à coller dans « Titre » :

```text
Questions fréquentes
```
**Corps (français)** — à coller dans le corps de page (bouton `</>` pour le HTML) :

```html
<p class="eyebrow">Aide</p>
<h2>Questions fréquentes</h2>
<h3>Comment se passe le paiement ?</h3>
<p>Vous payez à la livraison, en espèces, au moment de recevoir votre colis. Aucun paiement en ligne n'est demandé.</p>
<h3>Livrez-vous partout en Algérie ?</h3>
<p>Oui, dans les 69 wilayas, à domicile ou en stop-desk.</p>
<h3>Comment sont calculés les frais de livraison ?</h3>
<p>Les frais dépendent de la wilaya et du mode choisi. Le tarif s'affiche dans le formulaire de commande dès que vous sélectionnez votre wilaya et votre commune.</p>
<h3>Quels sont les délais de livraison ?</h3>
<p>2 à 5 jours ouvrés selon la wilaya. <em>(Délai de démonstration, à confirmer selon le transporteur.)</em></p>
<h3>Puis-je échanger un article ?</h3>
<p>Un échange est possible sous 7 jours, article non utilisé et dans son emballage d'origine. <em>(Conditions de démonstration.)</em></p>
<h3>Les produits sont-ils lavables ?</h3>
<p>Les textiles se lavent en machine à 30 °C, sauf indication contraire sur la fiche du produit.</p>
<h3>Puis-je commander sans créer de compte ?</h3>
<p>Oui. La commande se fait directement depuis la fiche produit : nom, téléphone, wilaya et commune suffisent.</p>
<h3>Comment vous contacter ?</h3>
<p>Notre service client répond sur WhatsApp et par e-mail : les coordonnées sont dans le pied de page et sur la page Contact.</p>
<p><a href="/pages/contact">Une autre question ? Écrivez-nous</a></p>
```
**Titre (arabe)** — dans « Traduire et adapter » :

```text
الأسئلة الشائعة
```
**Corps (arabe)** :

```html
<p class="eyebrow">المساعدة</p>
<h2>الأسئلة الشائعة</h2>
<h3>كيف يتم الدفع؟</h3>
<p>تدفعين عند الاستلام، نقدًا، لحظة تسلّم الطرد. لا نطلب أي دفع عبر الإنترنت.</p>
<h3>هل توصّلون إلى كل الجزائر؟</h3>
<p>نعم، إلى الولايات الـ 69، إلى المنزل أو إلى مكتب الاستلام.</p>
<h3>كيف تُحسب تكاليف التوصيل؟</h3>
<p>تتوقف التكلفة على الولاية ونوع التوصيل. يظهر السعر في نموذج الطلب بمجرد اختيار الولاية والبلدية.</p>
<h3>ما هي مدد التوصيل؟</h3>
<p>من 2 إلى 5 أيام عمل حسب الولاية. <em>(مدّة تجريبية، تُؤكَّد حسب شركة التوصيل.)</em></p>
<h3>هل يمكنني تبديل منتج؟</h3>
<p>التبديل ممكن في غضون 7 أيام، شرط أن يكون المنتج غير مستعمل وفي غلافه الأصلي. <em>(شروط تجريبية.)</em></p>
<h3>هل المنتجات قابلة للغسل؟</h3>
<p>الأقمشة تُغسل في الغسالة على 30 °م، إلا إذا ذُكر خلاف ذلك في وصف المنتج.</p>
<h3>هل يمكنني الطلب بدون إنشاء حساب؟</h3>
<p>نعم. يتم الطلب مباشرة من صفحة المنتج: الاسم ورقم الهاتف والولاية والبلدية تكفي.</p>
<h3>كيف أتواصل معكم؟</h3>
<p>يجيبك فريقنا على واتساب وبالبريد: البيانات موجودة في تذييل الصفحة وفي صفحة «اتصلي بنا».</p>
<p><a href="/pages/contact">سؤال آخر؟ راسلينا</a></p>
```

### 1.9 — Club Maman

* handle : `club-maman` → adresse `/pages/club-maman`

**Titre (français)** — à coller dans « Titre » :

```text
Club Maman
```
**Corps (français)** — à coller dans le corps de page (bouton `</>` pour le HTML) :

```html
<p class="eyebrow">Espace d'échange</p>
<h2>Club Maman</h2>
<p>Le Club Maman est l'espace d'échange de LLUFAN : poser une question, partager une astuce, lire l'expérience d'autres mamans.</p><p>Ici on parle du quotidien — le projet bébé, la grossesse, l'allaitement, les premiers mois — sans jugement et sans conseil médical.</p><p><em>Texte de démonstration.</em></p>
<h3>Nos espaces d'échange</h3>
<p><strong>Projet bébé</strong><br>Vous préparez l'arrivée de bébé : listes, chambre, premiers achats et questions pratiques.</p>
<p><strong>Grossesse</strong><br>Confort, sommeil, positions, préparation : échangez sur les mois qui précèdent la naissance.</p>
<p><strong>Allaitement</strong><br>Positions, matériel, rythme des tétées : les astuces de celles qui sont passées par là.</p>
<p><strong>Après la naissance</strong><br>Le quotidien avec bébé : nuits, rythme, organisation, et le droit de souffler un peu.</p>
<h3>Discussions</h3>
<h3>Quelle position pour allaiter la nuit ?</h3>
<p>Discussion de démonstration : bébé a cinq semaines et je cherche une position qui me permette de me reposer un peu…</p>
<p><em>Amina</em></p>
<h3>Préparer sa valise pour la maternité</h3>
<p>Discussion de démonstration : voici ma liste, dites-moi ce que j'ai oublié.</p>
<p><em>Lila</em></p>
<h3>Les nuits hachées, comment vous tenez ?</h3>
<p>Discussion de démonstration : je ne sais pas si c'est normal à trois semaines…</p>
<p><em>Nour</em></p>
<h3>Ressources pour les mamans</h3>
<p>Nos réponses aux questions les plus fréquentes : commande, paiement à la livraison, délais, entretien des produits.</p><p><em>Emplacement de démonstration : guides, articles ou vidéos viendront ici.</em></p>
<h3>Rejoindre le Club Maman</h3>
<p>Laissez votre e-mail pour être prévenue de l'ouverture des discussions et recevoir les conseils LLUFAN.</p><p><em>Texte de démonstration.</em></p>
<p>Inscription de démonstration : indiquez ici la finalité (conseils, nouveautés) et renvoyez vers la politique de confidentialité.</p>
```
**Titre (arabe)** — dans « Traduire et adapter » :

```text
نادي المامان
```
**Corps (arabe)** :

```html
<p class="eyebrow">فضاء للتبادل</p>
<h2>نادي المامان</h2>
<p>نادي المامان هو فضاء التبادل لدى LLUFAN: اطرحي سؤالًا، شاركي نصيحة، واقرئي تجربة أمهات أخريات.</p><p>نتحدّث هنا عن اليومي — مشروع الطفل، الحمل، الإرضاع، الأشهر الأولى — بدون حكم وبدون نصيحة طبية.</p><p><em>نص تجريبي.</em></p>
<h3>فضاءات التبادل</h3>
<p><strong>مشروع الطفل</strong><br>تستعدّين لقدوم الطفل: القوائم، الغرفة، أولى المشتريات والأسئلة العملية.</p>
<p><strong>الحمل</strong><br>الراحة، النوم، الوضعيات، التحضير: تبادلي حول الأشهر التي تسبق الولادة.</p>
<p><strong>الإرضاع</strong><br>الوضعيات، الأدوات، إيقاع الجلسات: نصائح من مررن من التجربة قبلك.</p>
<p><strong>بعد الولادة</strong><br>اليومي مع الطفل: الليالي، الإيقاع، التنظيم، وحقّ في أن تلتقطي أنفاسك.</p>
<h3>نقاشات</h3>
<h3>أي وضعية للإرضاع في الليل؟</h3>
<p>نقاش تجريبي: طفلتي عمرها خمسة أسابيع وأبحث عن وضعية تسمح لي بالراحة قليلًا…</p>
<p><em>أمينة</em></p>
<h3>تحضير حقيبة الولادة</h3>
<p>نقاش تجريبي: هذه قائمتي، أخبرنني ما نسيت.</p>
<p><em>ليلى</em></p>
<h3>الليالي المتقطّعة، كيف تصمدن؟</h3>
<p>نقاش تجريبي: لا أعرف إن كان هذا عاديًا في الأسبوع الثالث…</p>
<p><em>نور</em></p>
<h3>مصادر للأمهات</h3>
<p>أجوبتنا عن أكثر الأسئلة تكرارًا: الطلب، الدفع عند الاستلام، المدد، العناية بالمنتجات.</p><p><em>مكان تجريبي: أدلّة ومقالات وفيديوهات ستأتي هنا.</em></p>
<h3>انضمي إلى نادي المامان</h3>
<p>اتركي بريدك الإلكتروني لتصلك انطلاقة النقاشات ونصائح LLUFAN.</p><p><em>نص تجريبي.</em></p>
<p>تسجيل تجريبي: يُذكر هنا الهدف (نصائح، جديد) مع الإحالة على سياسة الخصوصية.</p>
```

### 1.10 — Contact

* handle : `contact` → adresse `/pages/contact`

**Titre (français)** — à coller dans « Titre » :

```text
Contact
```
*Cette page est construite par le thème : seul le titre se remplit.*

**Titre (arabe)** — dans « Traduire et adapter » :

```text
اتصلي بنا
```

---

## 2. Les 5 collections

Produits → **Collections** → Créer une collection. Le handle doit être
exactement celui-ci : c'est lui que le thème appelle.

### Maternité — `maternite`

```text
Titre (français) : Maternité
```
```html
<p>Tout pour accompagner la grossesse et l'arrivée de bébé : coussins, confort du quotidien et essentiels de la chambre.</p><p><em>Collection de démonstration.</em></p>
```
```text
Titre (arabe) : الأمومة
```
```html
<p>كل ما يواكب الحمل واستقبال المولود الجديد: الوسادات، راحة اليومي وأساسيات غرفة الطفل.</p><p><em>مجموعة تجريبية.</em></p>
```

### Allaitement — `allaitement`

```text
Titre (français) : Allaitement
```
```html
<p>Le nécessaire pour des tétées confortables, à la maison comme en déplacement : coussin d'allaitement, housses, coussinets et ponchos.</p><p><em>Collection de démonstration.</em></p>
```
```text
Titre (arabe) : الإرضاع
```
```html
<p>كل ما يلزم لجلسات إرضاع مريحة، في البيت وخارجه: وسادة الإرضاع، الأغطية، حشوات الإرضاع والبونشو.</p><p><em>مجموعة تجريبية.</em></p>
```

### Bébé — `bebe`

```text
Titre (français) : Bébé
```
```html
<p>Des matières douces pour les premiers mois : gigoteuse, couverture nid, bavoirs et sac à langer.</p><p><em>Collection de démonstration.</em></p>
```
```text
Titre (arabe) : الطفل
```
```html
<p>أقمشة ناعمة للأشهر الأولى: كيس النوم، بطانية العش، المرايل وحقيبة الحفاضات.</p><p><em>مجموعة تجريبية.</em></p>
```

### Nouveautés — `nouveautes`

```text
Titre (français) : Nouveautés
```
```html
<p>Les dernières pièces arrivées chez LLUFAN.</p><p><em>Collection de démonstration.</em></p>
```
```text
Titre (arabe) : الجديد
```
```html
<p>آخر ما وصل إلى LLUFAN.</p><p><em>مجموعة تجريبية.</em></p>
```

### Accessoires et pièces détachées — `accessoires`

```text
Titre (français) : Accessoires et pièces détachées
```
```html
<p>Housses de rechange, coussinets, bavoirs et petites pièces utiles au quotidien.</p><p><em>Collection de démonstration.</em></p>
```
```text
Titre (arabe) : الإكسسوارات وقطع الغيار
```
```html
<p>أغطية بديلة، حشوات الإرضاع، مرايل وقطع صغيرة مفيدة في اليومي.</p><p><em>مجموعة تجريبية.</em></p>
```

---

## 3. Le journal et ses 3 articles

Contenu → **Blog posts** → Gérer les blogs → Ajouter un blog (`Le journal`),
puis les trois articles.

```text
Nom du blog (français) : Le journal
Nom du blog (arabe)    : المجلة
```

### Comment choisir son coussin d'allaitement

* handle : `choisir-son-coussin-d-allaitement`

```text
Titre (français) : Comment choisir son coussin d'allaitement
Auteur : L'équipe LLUFAN
```
```html
<p><em>Forme, garnissage, entretien : les questions à se poser avant d'acheter (article de démonstration).</em></p>
<p><em>Article de démonstration, à remplacer par un texte validé par LLUFAN.</em></p><h2>La forme</h2><p>Un coussin en forme de boomerang se place autour du corps et sert d'appui pour les bras ; sa taille compte plus que son épaisseur. Les modèles longs en U conviennent mieux à celles qui cherchent un appui pour le dos et les jambes, pendant la grossesse comme après.</p><h2>Le garnissage</h2><p>Des microbilles suivent les positions et se remettent en forme d'un geste. Un garnissage trop ferme maintient sans se creuser ; trop souple, il s'affaisse vite.</p><h2>L'entretien</h2><p>Une housse déhoussable qui passe en machine à 30 °C change la vie : elle se lave souvent, et une housse de rechange permet de continuer à utiliser le coussin pendant le séchage.</p><p>Pour toute question liée à votre santé ou à celle de votre bébé, parlez-en à votre sage-femme ou à votre médecin.</p>
```
```text
Titre (arabe) : كيف تختارين وسادة الإرضاع المناسبة
Auteur : فريق LLUFAN
```
```html
<p><em>الشكل، الحشو، العناية: الأسئلة التي تُطرح قبل الشراء (مقال تجريبي).</em></p>
<p><em>مقال تجريبي، يُستبدل بنصّ معتمد من LLUFAN.</em></p><h2>الشكل</h2><p>الوسادة بشكل الهلال تُوضع حول الجسم وتكون مسندًا للذراعين؛ مقاسها أهمّ من سماكتها. الموديلات الطويلة على شكل U تناسب أكثر من تبحث عن سند للظهر والساقين، أثناء الحمل وبعده.</p><h2>الحشو</h2><p>الكريات الدقيقة تتبع الوضعيات وتعود إلى شكلها بحركة واحدة. الحشو الصلب جدًا يسند دون أن ينخفض؛ والطري جدًا يهبط بسرعة.</p><h2>العناية</h2><p>غطاء قابل للفصل يُغسل في الغسالة على 30 °م يغيّر كل شيء: يُغسل كثيرًا، وغطاء احتياطي يسمح بمواصلة استعمال الوسادة في الأثناء.</p><h2>الخلاصة</h2><p>ابدئي من طريقة استعمالك: جلسات كثيرة في البيت، أو إرضاع في التنقل. الشكل يتبع ذلك.</p>
```

### Préparer ses premières tétées : l'organisation pratique

* handle : `preparer-ses-premieres-tetees`

```text
Titre (français) : Préparer ses premières tétées : l'organisation pratique
Auteur : L'équipe LLUFAN
```
```html
<p><em>Ce qui aide à se sentir prête, matériel et confort, sans prétendre remplacer un accompagnement (article de démonstration).</em></p>
<p><em>Article de démonstration, à remplacer par un texte validé par LLUFAN.</em></p><h2>Un endroit confortable</h2><p>Un fauteuil avec des accoudoirs, un coussin pour poser bébé à la bonne hauteur, et de la lumière douce : ce sont les trois éléments qui reviennent le plus dans les retours des mamans.</p><h2>À portée de main</h2><p>De l'eau, un téléphone chargé, un lange et la télécommande : la tétée dure le temps qu'elle dure, et se lever pour chercher un verre d'eau est rarement possible.</p><h2>S'entourer</h2><p>Les premiers jours soulèvent beaucoup de questions. Une sage-femme, une consultante en lactation ou une amie qui est passée par là valent mieux qu'une recherche sur internet à trois heures du matin. Le Club Maman existe pour ces échanges du quotidien — jamais pour remplacer un avis professionnel.</p>
```
```text
Titre (arabe) : التحضير لأولى جلسات الإرضاع: التنظيم العملي
Auteur : فريق LLUFAN
```
```html
<p><em>ما يساعدك على الشعور بالاستعداد، من الأدوات والراحة، دون أن يغني عن المرافقة (مقال تجريبي).</em></p>
<p><em>مقال تجريبي، يُستبدل بنصّ معتمد من LLUFAN.</em></p><h2>مكان مريح</h2><p>كرسي بمسندين، ووسادة ترفع الطفل إلى الارتفاع المناسب، وضوء هادئ: هذه العناصر الثلاثة هي الأكثر تكرارًا في تجارب الأمهات.</p><h2>في متناول اليد</h2><p>ماء، هاتف مشحون، قماش قطني وجهاز التحكّم: جلسة الإرضاع تدوم ما تدوم، والقيام للبحث عن كأس ماء نادرًا ما يكون ممكنًا.</p><h2>أحطي نفسك</h2><p>الأيام الأولى تطرح أسئلة كثيرة. قابلة أو مستشارة إرضاع أو صديقة مرّت من التجربة أفضل من بحث على الإنترنت في الثالثة صباحًا. نادي المامان موجود لهذه التبادلات.</p>
```

### La chambre de bébé : les essentiels des premiers mois

* handle : `la-chambre-de-bebe-les-essentiels`

```text
Titre (français) : La chambre de bébé : les essentiels des premiers mois
Auteur : L'équipe LLUFAN
```
```html
<p><em>Une liste courte, pour ne pas acheter tout ce qui brille (article de démonstration).</em></p>
<p><em>Article de démonstration, à remplacer par un texte validé par LLUFAN.</em></p><h2>Pour dormir</h2><p>Un berceau ou un lit conforme, un matelas ferme à sa taille, une gigoteuse adaptée à la saison. Les coussins, tours de lit et couvertures n'ont pas leur place dans le lit de bébé.</p><h2>Pour le change</h2><p>Une table à langer ou un plan stable, des couches, des lingettes ou des carrés de coton, une crème de change, et une réserve à portée de main.</p><h2>Pour les moments d'éveil</h2><p>Une couverture au sol, un tapis d'éveil, deux ou trois jouets : largement de quoi commencer. Le reste viendra au rythme de bébé.</p>
```
```text
Titre (arabe) : غرفة الطفل: الأساسيات في الأشهر الأولى
Auteur : فريق LLUFAN
```
```html
<p><em>قائمة قصيرة، لكي لا تشتري كل ما يلمع (مقال تجريبي).</em></p>
<p><em>مقال تجريبي، يُستبدل بنصّ معتمد من LLUFAN.</em></p><h2>للنوم</h2><p>سرير مطابق للمعايير، ومرتبة صلبة بمقاسه، وكيس نوم مناسب للفصل. الوسادات وأسوار السرير والأغطية ليس لها مكان في سرير الطفل.</p><h2>للتغيير</h2><p>طاولة تغيير أو سطح ثابت، حفاضات، مناديل أو مربّعات قطنية، كريم تغيير، ومخزون في متناول اليد.</p><h2>لفترات اللعب</h2><p>غطاء على الأرض، سجّادة لعب، ولعبتان أو ثلاث: هذا يكفي للبداية. والباقي يأتي على إيقاع الطفل.</p>
```

---

## 4. Ce qui n'est pas ici

- **Les produits** : ils s'importent par le fichier `LLUFAN-DEMO-produits.csv`
  (Produits → Importer), puis leurs traductions par le fichier
  `LLUFAN-DEMO-traductions-ar.csv`.
- **Les libellés de l'interface** (Panier, Filtrer, Votre nom, les messages
  du formulaire de commande) : ils sont déjà traduits dans le thème, fichier
  `locales/ar.json`, et partent avec lui.
- **Les pages Recherche, Compte et Page introuvable** : ce sont des gabarits
  du thème, rien à créer.

---

## 5. Les emplacements à compléter — le seul reste à faire

Ces mentions sont **volontaires** : elles marquent les informations que
seule LLUFAN peut fournir (raison sociale, hébergeur, qui paie le retour…).
Tout le reste des pages est complet et publiable tel quel.

| Réf. | Page | Langue | Ce qui manque |
|---|---|---|---|
| 1.4 | Échanges et retours | français | Emplacement à compléter : qui prend en charge les frais de retour (à décider par LLUFAN). |
| 1.5 | Mentions légales | français | [raison sociale, adresse et registre de commerce à compléter] |
| 1.5 | Mentions légales | français | [Nom et adresse de l'hébergeur à compléter] |
| 1.5 | Mentions légales | français | [Mentions relatives aux contenus, aux photos et à la marque à compléter] |
| 1.6 | Conditions générales de vente | français | [Objet des conditions de vente et champ d'application à compléter.] |
| 1.6 | Conditions générales de vente | français | [Délais et transporteurs à compléter.] |
| 1.6 | Conditions générales de vente | français | [Conditions d'échange et de retour à compléter.] |
| 1.7 | Politique de confidentialité | français | Gabarit de démonstration : à compléter selon les traitements réellement effectués. |
| 1.7 | Politique de confidentialité | arabe | نموذج تجريبي: يُستكمل حسب المعالجات الفعلية للبيانات. |
| 3.1 | Comment choisir son coussin d'allaitement | français | Article de démonstration, à remplacer par un texte validé par LLUFAN. |
| 3.1 | Comment choisir son coussin d'allaitement | arabe | مقال تجريبي، يُستبدل بنصّ معتمد من LLUFAN. |
| 3.2 | Préparer ses premières tétées : l'organisation pratique | français | Article de démonstration, à remplacer par un texte validé par LLUFAN. |
| 3.2 | Préparer ses premières tétées : l'organisation pratique | arabe | مقال تجريبي، يُستبدل بنصّ معتمد من LLUFAN. |
| 3.3 | La chambre de bébé : les essentiels des premiers mois | français | Article de démonstration, à remplacer par un texte validé par LLUFAN. |
| 3.3 | La chambre de bébé : les essentiels des premiers mois | arabe | مقال تجريبي، يُستبدل بنصّ معتمد من LLUFAN. |

**Règle simple : une page qui contient encore une de ces mentions ne se
publie pas.** Le plus souvent, une phrase suffit — et si une information
manque encore, mieux vaut retirer la phrase que la laisser en l'état.

