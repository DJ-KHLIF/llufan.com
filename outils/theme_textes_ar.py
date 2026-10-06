# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
#  LLUFAN — les textes du thème, en arabe.

#  POURQUOI CE FICHIER
#  Un audit du 6 octobre 2026 l'a relevé : « le thème possède de nombreuses
#  traductions arabes, mais plusieurs textes personnalisés restent sans
#  traduction : titres et boutons de l'accueil, réassurance, blocs produit, FAQ,
#  en-tête et pied de page ». C'est exact : les 23 premières lignes
#  ONLINE_STORE_THEME du fichier de traductions ne couvraient que les réglages
#  communs (bandeau, pré-bandeau, pied de page, Club Maman).
#  Les textes saisis DANS les gabarits du thème — accueil, fiche produit,
#  pages d'information, FAQ — n'étaient pas traduits : une cliente en arabe
#  voyait donc des blocs en français au milieu de la page.

#  CE QUE FAIT CE FICHIER
#  Il donne la traduction arabe de chaque texte français écrit dans le thème
#  (`templates/*.json` et `sections/*-group.json`). Le générateur
#  `generer_kit_shopify.py` s'en sert pour écrire une ligne ONLINE_STORE_THEME
#  par texte : une ligne = un champ, à coller dans l'export de traductions
#  Shopify (Paramètres → Langues → Exporter / Importer).

#  DEUX RÈGLES, TENUES VOLONTAIREMENT
#    1. Les textes qui portent une mention de DÉMONSTRATION la gardent en
#       arabe (« نص تجريبي », « نموذج تجريبي ») : une page traduite ne doit pas
#       faire oublier qu'elle n'est pas encore validée.
#    2. Aucune promesse de santé. L'audit demande d'éviter « les promesses de
#       soulagement qui ne peuvent pas être justifiées » : les traductions
#       parlent de confort, de douceur, d'entretien — jamais de soigner.

#  QUALITÉ LINGUISTIQUE : ces textes sont des PROPOSITIONS, comme ceux des
#  pages. Ils doivent être relus par un arabophone avant publication.

#  Comment le fichier est utilisé : par le texte français exact. Si un texte du
#  thème n'a pas sa traduction ici, le générateur s'arrête et le dit — jamais
#  de trou silencieux.
# ---------------------------------------------------------------------------

TEXTES_AR = {

    # ── Pages d'information : titres de blocs numérotés ─────────────────────
    "1. Données collectées": "1. البيانات المجمَّعة",
    "1. Nous contacter": "1. اتصلي بنا",
    "1. Objet": "1. الموضوع",
    "2. Délai": "2. المدّة",
    "2. Prix et devise": "2. الأسعار والعملة",
    "2. Utilisation": "2. الاستعمال",
    "3. Commande et paiement": "3. الطلب والدفع",
    "3. Conservation": "3. مدّة الحفظ",
    "3. État du produit": "3. حالة المنتج",
    "4. Destinataires": "4. الجهات المستفيدة",
    "4. Frais de retour": "4. مصاريف الإرجاع",
    "4. Livraison": "4. التوصيل",
    "5. Vos droits": "5. حقوقك",
    "5. Échanges et retours": "5. التبديل والإرجاع",
    "6. Service client": "6. خدمة العملاء",

    # ── Pages d'information : paragraphes ───────────────────────────────────
    "<p>2 à 5 jours ouvrés selon la wilaya. <em>(Délai de démonstration, à confirmer selon le transporteur.)</em></p>":
        "<p>من 2 إلى 5 أيام عمل حسب الولاية. <em>(مدّة تجريبية، تُؤكَّد حسب شركة التوصيل.)</em></p>",
    "<p><em>Ce gabarit ne remplace pas un texte juridique validé.</em></p>":
        "<p><em>هذا النموذج لا يغني عن نصّ قانوني معتمد.</em></p>",
    "<p><em>Délais indicatifs de démonstration : 2 à 5 jours ouvrés selon la wilaya (à confirmer selon le transporteur).</em></p>":
        "<p><em>مدّة إرشادية تجريبية: من 2 إلى 5 أيام عمل حسب الولاية (تُؤكَّد حسب شركة التوصيل).</em></p>",
    "<p><em>Emplacement à compléter : qui prend en charge les frais de retour (à décider par LLUFAN).</em></p>":
        "<p><em>موضع يُستكمل: من يتحمّل مصاريف الإرجاع (قرار LLUFAN).</em></p>",
    "<p><em>Gabarit de démonstration : ce texte présente la structure attendue et doit être validé avant la mise en ligne.</em></p>":
        "<p><em>نموذج تجريبي: يعرض هذا النص البنية المتوقّعة، ويجب اعتماده قبل النشر.</em></p>",
    "<p><em>Gabarit de démonstration : à compléter selon les traitements réellement effectués.</em></p>":
        "<p><em>نموذج تجريبي: يُستكمل حسب المعالجات الفعلية للبيانات.</em></p>",
    "<p><em>Gabarit de démonstration, sans valeur juridique.</em></p>":
        "<p><em>نموذج تجريبي، بدون قيمة قانونية.</em></p>",
    "<p><em>Page de démonstration : complétez les informations ci-dessous avant la mise en ligne.</em></p>":
        "<p><em>صفحة تجريبية: أكملي المعلومات أدناه قبل النشر.</em></p>",
    "<p><em>Page de démonstration. Remplacer par la politique de retour validée par LLUFAN.</em></p>":
        "<p><em>صفحة تجريبية. تُستبدل بسياسة الإرجاع المعتمدة من LLUFAN.</em></p>",
    "<p><em>[Conditions d'échange et de retour à compléter.]</em></p>":
        "<p><em>[شروط التبديل والإرجاع تُستكمل.]</em></p>",
    "<p><em>[Durée de conservation à définir.]</em></p>":
        "<p><em>[مدّة الحفظ تُحدَّد.]</em></p>",
    "<p><em>[Mentions relatives aux contenus, aux photos et à la marque à compléter]</em>.</p>":
        "<p><em>[إشارات المحتوى والصور والعلامة تُستكمل]</em>.</p>",
    "<p><em>[Nom et adresse de l'hébergeur à compléter]</em>.</p>":
        "<p><em>[اسم المضيف وعنوانه يُستكملان]</em>.</p>",
    "<p><em>[Objet des conditions de vente et champ d'application à compléter.]</em></p>":
        "<p><em>[موضوع شروط البيع ونطاق التطبيق يُستكملان.]</em></p>",
    "<p>Aucune carte bancaire n'est demandée sur le site : vous commandez, nous vous rappelons, et vous payez en espèces quand le colis vous est remis.</p>":
        "<p>لا تُطلب أي بطاقة بنكية على الموقع: تُقدّمين الطلب، نتّصل بك، وتدفعين نقدًا عند تسليم الطرد.</p>",
    "<p>Aucune discussion pour le moment. Elles s'afficheront ici dès que le Club Maman ouvrira ses portes.</p>":
        "<p>لا نقاشات في الوقت الحالي. ستظهر هنا بمجرّد افتتاح نادي الأمهات.</p>",
    "<p>Avant l'expédition, nous vérifions le récapitulatif, l'adresse et le numéro de téléphone.</p>":
        "<p>قبل الإرسال، نتحقّق من الملخّص والعنوان ورقم الهاتف.</p>",
    "<p>Ces données servent uniquement à traiter la commande, organiser la livraison et assurer le service client.</p>":
        "<p>تُستعمل هذه البيانات فقط لمعالجة الطلب وتنظيم التوصيل وخدمة العملاء.</p>",
    "<p>Chaque produit LLUFAN est pensé pour un usage simple au quotidien. Les indications détaillées figurent dans la description du produit.</p><p><em>Texte de démonstration.</em></p>":
        "<p>كل منتج من LLUFAN مصمَّم لاستعمال بسيط في اليومي. التفاصيل الكاملة في وصف المنتج.</p><p><em>نص تجريبي.</em></p>",
    "<p>Chaque produit part d'un besoin réel du quotidien, avec un principe : faire simple et solide.</p>":
        "<p>كل منتج ينطلق من حاجة حقيقية في اليومي، بمبدأ واحد: البساطة والمتانة.</p>",
    "<p>Des formes qui accompagnent le corps, des matières douces sur la peau de bébé.</p>":
        "<p>أشكال ترافق الجسم، ومواد ناعمة على بشرة الطفل.</p>",
    "<p>Des matières et des finitions pensées pour être utilisées longtemps.</p>":
        "<p>مواد وتشطيبات مدروسة لتدوم طويلاً.</p>",
    "<p>L'article doit être non utilisé et dans son emballage d'origine.</p>":
        "<p>يجب أن يكون المنتج غير مستعمل وفي تغليفه الأصلي.</p>",
    "<p>LLUFAN est née d'un constat simple : en Algérie, les mamans cherchent des produits doux, bien pensés, et un interlocuteur qui répond vraiment. Nous imaginons des produits pour la grossesse, l'allaitement et les premiers mois de bébé, avec une attention particulière portée au confort et à la simplicité au quotidien.</p><p><em>Texte de démonstration : cette page sera remplacée par l'histoire, les valeurs et la fabrication telles que LLUFAN souhaite les raconter.</em></p>":
        "<p>وُلدت LLUFAN من ملاحظة بسيطة: في الجزائر، تبحث الأمّهات عن منتجات ناعمة، مدروسة بعناية، وعن جهة تُجيب بصدق. نصمّم منتجات لفترة الحمل والرضاعة والأشهر الأولى من عمر الطفل، بعناية خاصة بالراحة والبساطة في اليومي.</p><p><em>نص تجريبي: ستُستبدل هذه الصفحة بحكاية العلامة وقيمها وطريقة التصنيع كما تحبّ LLUFAN أن ترويها.</em></p>",
    "<p>LLUFAN — <em>[raison sociale, adresse et registre de commerce à compléter]</em>.</p>":
        "<p>LLUFAN — <em>[الاسم التجاري والعنوان والسجل التجاري تُستكمل]</em>.</p>",
    "<p>La commande se fait sur le site, sans paiement en ligne : le règlement se fait en espèces à la livraison (COD).</p>":
        "<p>يُقدَّم الطلب على الموقع دون دفع إلكتروني: الدفع نقدًا عند الاستلام.</p>",
    "<p>La composition précise est indiquée sur la fiche de chaque produit.</p><p><em>Emplacement de démonstration : composition détaillée et origine des matières.</em></p>":
        "<p>التركيبة الدقيقة مذكورة في صفحة كل منتج.</p><p><em>موضع تجريبي: التركيبة المفصّلة ومصدر المواد.</em></p>",
    "<p>La demande est à faire sous 7 jours après la réception du colis. <em>(Durée de démonstration, à valider.)</em></p>":
        "<p>يُقدَّم الطلب خلال 7 أيام من استلام الطرد. <em>(مدّة تجريبية، تحتاج تأكيدًا.)</em></p>",
    "<p>Laissez votre e-mail pour être prévenue de l'ouverture des discussions et recevoir les conseils LLUFAN.</p><p><em>Texte de démonstration.</em></p>":
        "<p>اتركي بريدك الإلكتروني ليصلك إشعار فتح النقاشات ونصائح LLUFAN.</p><p><em>نص تجريبي.</em></p>",
    "<p>Lavage en machine à 30 °C recommandé pour les textiles. Séchage à l'air libre. Ne pas utiliser d'eau de javel.</p><p><em>Texte de démonstration.</em></p>":
        "<p>يُنصح بغسل المنسوجات في الغسالة عند 30 °م. التجفيف في الهواء الطلق. يُمنع استعمال ماء الجافيل.</p><p><em>نص تجريبي.</em></p>",
    "<p>Le Club Maman est l'espace d'échange de LLUFAN : poser une question, partager une astuce, lire l'expérience d'autres mamans.</p><p>Ici on parle du quotidien — le projet bébé, la grossesse, l'allaitement, les premiers mois — sans jugement et sans conseil médical.</p><p><em>Texte de démonstration.</em></p>":
        "<p>نادي الأمهات هو فضاء التبادل في LLUFAN: اطرحي سؤالاً، شاركي نصيحة، واقرئي تجربة أمّهات أخريات.</p><p>نتحدّث هنا عن اليومي — مشروع الطفل، الحمل، الرضاعة، الأشهر الأولى — بدون حكم وبدون نصيحة طبية.</p><p><em>نص تجريبي.</em></p>",
    "<p>Le montant est réglé en espèces au livreur, au moment de la remise du colis.</p>":
        "<p>يُدفع المبلغ نقدًا لعامل التوصيل عند تسليم الطرد.</p>",
    "<p>Le site ne demande ni carte bancaire ni virement. La commande est confirmée par téléphone ou par WhatsApp.</p>":
        "<p>لا يطلب الموقع بطاقة بنكية ولا تحويلاً. يُؤكَّد الطلب هاتفيًا أو عبر واتساب.</p>",
    "<p>Le tarif dépend de la wilaya et du mode de livraison. Il apparaît dès que vous choisissez votre wilaya et votre commune dans le formulaire de commande.</p>":
        "<p>تتحدّد التعريفة حسب الولاية وطريقة التوصيل، وتظهر مباشرة بعد اختيار الولاية والبلدية في استمارة الطلب.</p>",
    "<p>Les 69 wilayas d'Algérie, à domicile ou en stop-desk.</p><p><em>Tarifs de démonstration : ils seront remplacés par les tarifs transporteur réels.</em></p>":
        "<p>الولايات الـ69 في الجزائر، إلى المنزل أو إلى مكتب الاستلام.</p><p><em>أسعار تجريبية: ستُستبدل بأسعار شركة التوصيل الفعلية.</em></p>",
    "<p>Les frais dépendent de la wilaya et du mode choisi. Le tarif s'affiche dans le formulaire de commande dès que vous sélectionnez votre wilaya et votre commune.</p>":
        "<p>تتحدّد المصاريف حسب الولاية والطريقة المختارة، وتظهر في استمارة الطلب بعد اختيار الولاية والبلدية.</p>",
    "<p>Les informations saisies dans le formulaire de commande : nom, numéro de téléphone, wilaya, commune, mode de livraison, contenu du panier.</p>":
        "<p>المعلومات المُدخَلة في استمارة الطلب: الاسم، رقم الهاتف، الولاية، البلدية، طريقة التوصيل، ومحتوى السلة.</p>",
    "<p>Les informations strictement nécessaires sont transmises au transporteur chargé de la livraison.</p>":
        "<p>تُسلَّم المعلومات الضرورية فقط إلى شركة التوصيل المكلّفة بالعملية.</p>",
    "<p>Les textiles se lavent en machine à 30 °C, sauf indication contraire sur la fiche du produit.</p>":
        "<p>تُغسل المنسوجات في الغسالة عند 30 °م، إلا إذا ذُكر خلاف ذلك في صفحة المنتج.</p>",
    "<p>Livraison dans les 69 wilayas, à domicile ou en stop-desk. <em>[Délais et transporteurs à compléter.]</em></p>":
        "<p>التوصيل إلى الولايات الـ69، إلى المنزل أو إلى مكتب الاستلام. <em>[المدّة وشركات التوصيل تُستكملان.]</em></p>",
    "<p>Nos coordonnées (WhatsApp et e-mail) sont indiquées dans le pied de page et sur la page Contact.</p>":
        "<p>بيانات التواصل (واتساب والبريد الإلكتروني) مذكورة في أسفل الصفحة وفي صفحة الاتصال.</p>",
    "<p>Nos réponses aux questions les plus fréquentes : commande, paiement à la livraison, délais, entretien des produits.</p><p><em>Emplacement de démonstration : guides, articles ou vidéos viendront ici.</em></p>":
        "<p>أجوبتنا على أكثر الأسئلة تكرارًا: الطلب، الدفع عند الاستلام، المدّة، العناية بالمنتجات.</p><p><em>موضع تجريبي: أدلّة أو مقالات أو فيديوهات ستُضاف هنا.</em></p>",
    "<p>Notre service client répond sur WhatsApp et par e-mail : les coordonnées sont dans le pied de page et sur la page Contact.</p>":
        "<p>خدمة العملاء تُجيب عبر واتساب والبريد الإلكتروني: البيانات في أسفل الصفحة وفي صفحة الاتصال.</p>",
    "<p>Notre service client répond sur WhatsApp et par e-mail, avant et après la commande.</p>":
        "<p>خدمة العملاء تُجيب عبر واتساب والبريد الإلكتروني، قبل الطلب وبعده.</p>",
    "<p>Notre équipe vous contacte pour confirmer la wilaya, la commune et le mode de livraison.</p>":
        "<p>يتّصل بك فريقنا لتأكيد الولاية والبلدية وطريقة التوصيل.</p>",
    "<p>Nous concevons des produits doux, faciles à entretenir et faits pour être utilisés longtemps, de la grossesse aux premiers mois de bébé.</p><p><em>Texte de démonstration.</em></p>":
        "<p>نصمّم منتجات ناعمة، سهلة العناية، ومصنوعة لتدوم: من الحمل إلى الأشهر الأولى من عمر الطفل.</p><p><em>نص تجريبي.</em></p>",
    "<p>Nous livrons dans les 69 wilayas, à domicile ou en stop-desk. Les frais sont calculés selon votre wilaya et le mode choisi, et s'affichent automatiquement dans le formulaire de commande.</p>":
        "<p>نوصّل إلى الولايات الـ69، إلى المنزل أو إلى مكتب الاستلام. تُحسب المصاريف حسب ولايتك والطريقة المختارة، وتظهر تلقائيًا في استمارة الطلب.</p>",
    "<p>Oui, dans les 69 wilayas, à domicile ou en stop-desk.</p>":
        "<p>نعم، إلى الولايات الـ69، إلى المنزل أو إلى مكتب الاستلام.</p>",
    "<p>Oui. La commande se fait directement depuis la fiche produit : nom, téléphone, wilaya et commune suffisent.</p>":
        "<p>نعم. يُقدَّم الطلب مباشرة من صفحة المنتج: الاسم والهاتف والولاية والبلدية تكفي.</p>",
    "<p>Pour connaître l'état de votre commande, contactez-nous sur WhatsApp.</p>":
        "<p>لمعرفة حالة طلبك، تواصلي معنا عبر واتساب.</p>",
    "<p>Tous les prix sont affichés en dinars algériens (DZD), frais de livraison en sus selon la wilaya.</p>":
        "<p>كل الأسعار بالدينار الجزائري (دج)، ومصاريف التوصيل تُضاف حسب الولاية.</p>",
    "<p>Un article ne convient pas ? Voici comment faire, étape par étape.</p><p><em>Gabarit de démonstration : les conditions définitives seront fixées par LLUFAN.</em></p>":
        "<p>منتج لا يناسبك؟ هذه الخطوات بالترتيب.</p><p><em>نموذج تجريبي: الشروط النهائية تحدّدها LLUFAN.</em></p>",
    "<p>Un échange est possible sous 7 jours, article non utilisé et dans son emballage d'origine. <em>(Conditions de démonstration.)</em></p>":
        "<p>التبديل ممكن خلال 7 أيام، بشرط أن يكون المنتج غير مستعمل وفي تغليفه الأصلي. <em>(شروط تجريبية.)</em></p>",
    "<p>Une tétée confortable, une sieste qui tient, un objet qu'on garde longtemps : notre travail commence par ces petits moments du quotidien.</p><p><em>Texte de démonstration à remplacer par l'éditorial LLUFAN.</em></p>":
        "<p>رضعة مريحة، قيلولة هادئة، وقطعة تُحفظ طويلاً: عملنا يبدأ من هذه اللحظات الصغيرة في اليومي.</p><p><em>نص تجريبي يُستبدل بنصّ LLUFAN التحريري.</em></p>",
    "<p>Une équipe joignable sur WhatsApp et par e-mail, avant comme après votre commande.</p>":
        "<p>فريق يمكن الوصول إليه عبر واتساب والبريد الإلكتروني، قبل الطلب وبعده.</p>",
    "<p>Vous payez en espèces à la réception du colis, une fois la commande livrée.</p>":
        "<p>تدفعين نقدًا عند استلام الطرد، بعد توصيل الطلب.</p>",
    "<p>Vous payez à la livraison, en espèces, au moment de recevoir votre colis. Aucun paiement en ligne n'est demandé.</p>":
        "<p>تدفعين عند التسليم، نقدًا، لحظة استلام الطرد. لا يُطلب أي دفع إلكتروني.</p>",
    "<p>Vous pouvez demander l'accès, la rectification ou la suppression de vos données en nous contactant.</p>":
        "<p>يمكنك طلب الوصول إلى بياناتك أو تصحيحها أو حذفها بالتواصل معنا.</p>",
    "<p>Écrivez-nous sur WhatsApp ou par e-mail en précisant votre numéro de commande et le produit concerné.</p>":
        "<p>راسلينا عبر واتساب أو البريد الإلكتروني مع ذكر رقم الطلب والمنتج المعني.</p>",

    # ── Pied de page et en-tête (les 17 réglages non couverts) ──────────────
    "Accessoires et pièces détachées": "الإكسسوارات وقطع الغيار",
    "Aide": "المساعدة",
    "Allaitement": "الرضاعة",
    "Après la naissance": "بعد الولادة",
    "Bébé": "الطفل",
    "CLUB MAMAN": "نادي الأمهات",
    "Conçu pour l'allaitement": "مصمَّم للرضاعة",
    "Contact": "اتصلي بنا",
    "Grossesse": "الحمل",
    "Livraison dans les 69 wilayas": "التوصيل إلى الولايات الـ69",
    "Livraison partout en Algérie": "التوصيل إلى كل الجزائر",
    "Maternité": "الأمومة",
    "Nos engagements": "التزاماتنا",
    "Nos univers": "عوالمنا",
    "Nouveautés": "المستجدات",
    "Projet bébé": "مشروع الطفل",
    "Service client LLUFAN": "خدمة عملاء LLUFAN",
    "Échanges et retours": "التبديل والإرجاع",

    # ── Accueil ─────────────────────────────────────────────────────────────
    "Chaque détail compte": "كل تفصيلة مهمّة",
    "Choisi pour durer": "مُختار ليدوم",
    "Confort maman et bébé": "راحة الأم والطفل",
    "Des matières douces, pensées pour le quotidien": "مواد ناعمة، مدروسة لليومي",
    "Découvrir": "اكتشفي",
    "Découvrir Nomad": "اكتشفي نوماد",
    "Découvrir la marque": "اكتشفي العلامة",
    "Elles en parlent": "يتحدّثن عنّا",
    "Le coussin d'allaitement Nomad": "وسادة الرضاعة نوماد",
    "Nos coups de cœur allaitement": "مختاراتنا للرضاعة",
    "Nouveau": "جديد",
    "Nouveauté": "مستجد",
    "Parce que": "لأنّ",
    "Voir toute la collection": "تصفّحي كل التشكيلة",
    "Vous préparez l'arrivée de bébé : listes, chambre, premiers achats et questions pratiques.":
        "تستعدّين لقدوم الطفل: القوائم، الغرفة، أول المشتريات، وأسئلة عملية.",

    # ── Avis de la page d'accueil (démonstration, à remplacer) ──────────────
    "Amina — Alger": "أمينة — الجزائر",
    "Sarah — Oran": "سارة — وهران",
    "Nour — Constantine": "نور — قسنطينة",
    "Avis de démonstration : commande passée le lundi, colis reçu en stop-desk le mercredi, paiement à la réception.":
        "رأي تجريبي: الطلب يوم الاثنين، والطرد وصل إلى مكتب الاستلام يوم الأربعاء، والدفع عند الاستلام.",
    "Avis de démonstration : le coussin tient bien en place et les tétées de nuit sont beaucoup plus simples.":
        "رأي تجريبي: الوسادة تثبت جيدًا والرضعات الليلية أصبحت أسهل بكثير.",
    "Avis de démonstration : le tissu est très doux et la housse passe en machine sans problème.":
        "رأي تجريبي: القماش ناعم جدًا والغطاء يُغسل في الغسالة بلا مشكلة.",

    # ── Fiche produit ───────────────────────────────────────────────────────
    "Aucun paiement en ligne": "بدون دفع إلكتروني",
    "Commande protégée": "طلب محميّ",
    "Commande vérifiée": "طلب مُتحقَّق منه",
    "Composition": "التركيبة",
    "Confirmation par WhatsApp": "تأكيد عبر واتساب",
    "Description": "الوصف",
    "Des produits pensés pour le quotidien": "منتجات مدروسة لليومي",
    "Entretien": "العناية",
    "Livraison 2 à 5 jours ouvrés": "التوصيل في 2 إلى 5 أيام عمل",
    "Sans paiement en ligne": "بدون دفع إلكتروني",
    "Utilisation": "الاستعمال",
    "Vous aimerez aussi": "قد يعجبك أيضًا",
    "Vous payez à la réception": "تدفعين عند الاستلام",
    "Vus récemment": "شوهدت مؤخّرًا",

    # ── Questions fréquentes (fiche produit, collections, page) ─────────────
    "Comment se passe le paiement ?": "كيف يتم الدفع؟",
    "Comment sont calculés les frais de livraison ?": "كيف تُحسب مصاريف التوصيل؟",
    "Comment vous contacter ?": "كيف تتواصلين معنا؟",
    "Les produits sont-ils lavables ?": "هل المنتجات قابلة للغسل؟",
    "Livrez-vous partout en Algérie ?": "هل توصّلون إلى كل الجزائر؟",
    "Puis-je commander sans créer de compte ?": "هل يمكنني الطلب دون إنشاء حساب؟",
    "Puis-je échanger un article ?": "هل يمكنني تبديل منتج؟",
    "Quels sont les délais de livraison ?": "ما هي مدّة التوصيل؟",
    "Questions fréquentes": "الأسئلة الشائعة",
    "Une autre question ? Écrivez-nous": "سؤال آخر؟ راسلينا",

    # ── Pages d'information : titres et libellés ────────────────────────────
    "Des produits pensés ici": "منتجات مدروسة هنا",
    "FAQ": "الأسئلة الشائعة",
    "Frais de livraison": "مصاريف التوصيل",
    "Paiement à la livraison": "الدفع عند الاستلام",
    "Hébergement": "الاستضافة",
    "Informations": "معلومات",
    "Le confort avant tout": "الراحة أولاً",
    "Nous contacter": "تواصلي معنا",
    "Nous écrire": "راسلينا",
    "Page contact": "صفحة الاتصال",
    "Page livraison": "صفحة التوصيل",
    "Pages paiement": "صفحات الدفع",
    "Propriété intellectuelle": "الملكية الفكرية",
    "Suivi de la commande": "تتبّع الطلب",
    "Un contact humain": "تواصل بشري",
    "Une marque algérienne, dédiée au confort de la maman et du bébé":
        "علامة جزائرية، مكرّسة لراحة الأم والطفل",
    "Voir tous nos produits": "تصفّحي كل منتجاتنا",
    "Zones desservies": "المناطق المخدومة",
    "Éditeur du site": "ناشر الموقع",

    # ── Club Maman ──────────────────────────────────────────────────────────
    "Amina": "أمينة",
    "Confort, sommeil, positions, préparation : échangez sur les mois qui précèdent la naissance.":
        "الراحة، النوم، الوضعيات، التحضير: تبادلي الحديث في الأشهر التي تسبق الولادة.",
    "Discussion de démonstration : bébé a cinq semaines et je cherche une position qui me permette de me reposer un peu…":
        "نقاش تجريبي: طفلي في الأسبوع الخامس وأبحث عن وضعية تسمح لي بالراحة قليلاً…",
    "Discussion de démonstration : je ne sais pas si c'est normal à trois semaines…":
        "نقاش تجريبي: لا أعرف إن كان هذا طبيعيًا في الأسبوع الثالث…",
    "Discussion de démonstration : voici ma liste, dites-moi ce que j'ai oublié.":
        "نقاش تجريبي: هذه قائمتي، أخبروني بما نسيت.",
    "Espace d'échange": "فضاء التبادل",
    "Inscription de démonstration : indiquez ici la finalité (conseils, nouveautés) et renvoyez vers la politique de confidentialité.":
        "تسجيل تجريبي: اذكري هنا الغاية (نصائح، مستجدات) وأحِيلي إلى سياسة الخصوصية.",
    "Le quotidien avec bébé : nuits, rythme, organisation, et le droit de souffler un peu.":
        "اليومي مع الطفل: الليالي، الإيقاع، التنظيم، والحقّ في التقاط الأنفاس.",
    "Les nuits hachées, comment vous tenez ?": "الليالي المتقطّعة، كيف تصمدين؟",
    "Lila": "ليلى",
    "Nour": "نور",
    "Positions, matériel, rythme des tétées : les astuces de celles qui sont passées par là.":
        "الوضعيات، العتاد، إيقاع الرضعات: نصائح من مررن من هنا.",
    "Préparer sa valise pour la maternité": "تحضير حقيبة الولادة",
    "Quelle position pour allaiter la nuit ?": "أي وضعية للرضاعة ليلاً؟",
    "Ressources pour les mamans": "موارد للأمّهات",
    "Voir la FAQ": "تصفّحي الأسئلة الشائعة",
    # ── Textes déjà traduits ailleurs dans le kit (rapatriés ici pour que le
    #    dictionnaire couvre à lui seul tout ce que le thème affiche) ──────────
    "Contenu de démonstration — à remplacer avant la mise en ligne.": "محتوى تجريبي — يُستبدل قبل النشر.",
    "Conditions générales de vente": "شروط البيع العامة",
    "Club Maman": "نادي المامان",
    "Nos espaces d'échange": "فضاءات التبادل",
    "Discussions": "نقاشات",
    "Rejoindre le Club Maman": "انضمي إلى نادي المامان",
    "Je m'inscris": "أشترك",
    "Merci, votre inscription est enregistrée.": "شكرًا، تم تسجيل اشتراكك.",
    "Créer mon compte": "إنشاء حسابي",
    "Contenu de démonstration — à remplacer avant la mise en ligne.": "محتوى تجريبي — يُستبدل قبل النشر.",
    "Politique de confidentialité": "سياسة الخصوصية",
    "Contenu de démonstration — à remplacer avant la mise en ligne.": "محتوى تجريبي — يُستبدل قبل النشر.",
    "La marque": "العلامة",
    "Commander": "إتمام الطلب",
    "Contenu de démonstration — à remplacer avant la mise en ligne.": "محتوى تجريبي — يُستبدل قبل النشر.",
    "Contenu de démonstration — à remplacer avant la mise en ligne.": "محتوى تجريبي — يُستبدل قبل النشر.",
    "Mentions légales": "المعلومات القانونية",
    "Contenu de démonstration — à remplacer avant la mise en ligne.": "محتوى تجريبي — يُستبدل قبل النشر.",
    "Contenu de démonstration — à remplacer avant la mise en ligne.": "محتوى تجريبي — يُستبدل قبل النشر.",
    "Commander — Paiement à la livraison": "اطلبي — الدفع عند الاستلام",
    "Commander maintenant": "اطلبي الآن",
    "Paiement à la livraison · 69 wilayas": "الدفع عند الاستلام · 69 ولاية",
    "Livraison à domicile ou en stop-desk": "التوصيل إلى المنزل أو إلى مكتب الاستلام",
    "Espace maman": "نادي الأمهات",
    "La marque": "العلامة",
    "Pièces détachées": "قطع الغيار",
    "Aide / FAQ": "المساعدة / الأسئلة الشائعة",
    "La marque": "العلامة",
    "Livraison": "التوصيل",
    "Paiement": "الدفع",
    "Tous droits réservés.": "جميع الحقوق محفوظة.",
    "Algérie · llufan.com": "الجزائر · llufan.com",
    "Mentions légales": "المعلومات القانونية",
    "Conditions générales de vente": "شروط البيع العامة",
    "Politique de confidentialité": "سياسة الخصوصية",
    "Politique de retour / échange": "التبديل والإرجاع",
}