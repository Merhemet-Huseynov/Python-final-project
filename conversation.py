import random

class Conversation:

    def order_dialogue(self, *args):
        if len(args) != 5:
            return "Yalnız 5 argument göndərə bilərsiz."

        order, decoration, weight, time, total_price = args

        # Müştəri və satıcı arasında sifariş zamanı dialoqlar:
        dialogue = [[
            f"\nMüştəri: Salam, bir tort 🎂 sifariş etmək istəyirəm. 🍰\n",
            f"Satıcı: Salam, buyurun necə bir tort 🎂 sifariş etmək istəyirsiniz? 🤔\n",
            f"Müştəri: {order} sifariş etmək istəyirəm, amma mütləq dadlı olsun! 😋\n",
            f"Müştəri: Tort 🎂 üçün dekorasiya əlavə edə bilərsinizmi? 🌸🎨\n",
            f"Satıcı: Bəli, əlbəttə, necə bir dekorasiya istəyirsiniz? 🌟🎀\n",
            f"Müştəri: {decoration} olsun, şokoladlı parçalar 🍫 çox gözəl olar.\n",
            f"Satıcı: Çox gözəl! Çəkisi nə qədər olsun? ⚖️\n",
            f"Müştəri: {weight} kq olsun, amma çox böyük olmasın! 🎂💪\n",
            f"Satıcı: Qeyd etdik, tortunuz {time} saat sonra hazır olacaq. ⏰🔜\n",
            f"Satıcı: Qiyməti {total_price} manat edir. 💵💰\n",
            f"{time} saat sonra...\n",
            f"Müştəri: Təkrar salamlar, sifariş hazırdır? 😊🎉\n",
            f"Satıcı: Salam, sizin sifariş hazırdır. 🎉🥳\n",
            f"Müştəri: Mükəmməl tort! Tortun pulunu buradan çıxın. 💳💖\n",
            f"Satıcı: Əla, bəyəndiyinizə sevindim. Buyurun, tortun çeki. 🧾💝\n"
        ],
        [
            f"\nMüştəri: Salam! Mən bir tort 🎂 sifariş etmək istəyirəm. 🍓🍰\n",
            f"Satıcı: Salam! Əla, necə bir tort 🎂 sifariş etmək istəyirsiniz? 🤔🎉\n",
            f"Müştəri: Mənə {order} lazımdır, amma ən dadlısını istəyirəm! 😋🍰\n",
            f"Satıcı: Əlbəttə, dekorasiyanı necə istərdiniz? 🌟🌸\n",
            f"Müştəri: Hmmm, çox maraqlı! {decoration} ilə bəzəsəniz əla olar. ✨🌼\n",
            f"Satıcı: Oooo, çox gözəl bir seçim! Tortun çəkisi nə qədər olsun? ⚖️🎂\n",
            f"Müştəri: {weight} kq lazımdır, amma balaca olmasın. Yeterli qədər böyük olsun. 🥳💪\n",
            f"Satıcı: Tamam, tortunuz {time} saat sonra hazır olacaq. ⏰🎉\n",
            f"Satıcı: Qiymət isə {total_price} manat olacaq. Razısınız? 💵💸\n",
            f"Müştəri: Hə, bəli! Mən tortu gözləyəcəyəm. 😄⏳\n",
            f"{time} saat sonra...\n",
            f"Müştəri: Salam! Tort hazırdır? 🎉🎂\n",
            f"Satıcı: Salam! Bəli, tortunuz hazırdır və çox gözəl alınıb. ✨🎉\n",
            f"Müştəri: Vay, necə də gözəl alınıb! Pulu burdan çıxın. 💳💖\n",
            f"Satıcı: Çox sağ olun, tortu bəyəndiyinizə sevindim. Buyurun, çeki də sizə təqdim edirəm. 🧾💐\n",
            f"Müştəri: Çox sağ olun! Hər şey mükəmməl oldu. 😍🎉\n"
        ]]

        # Random bir dialoq seçir
        random_sweet_dialogue = random.choice(dialogue)
        
        return random_sweet_dialogue



    def sweets_dialogue(self, *args):
        if len(args) != 3:
            return "Yalnız 3 argument göndərə bilərsiz."

        sweets, weight, total_price = args

        # Müştəri və satıcı arasında şirniyat alarkən keçən dialoqlar:
        dialogue = [
            [
                f"Müştəri: Salam, şirniyyat 🍩 almaq istəyirəm, köməklik edə bilərsiniz? 🍰\n",
                f"Satıcı: Salam, hansı növ şirniyyat 🍪 istəyirsiniz? 🤔\n",
                f"Müştəri: {sweets} 🍩 var? 🍫\n",         
                f"Satıcı: Bəli, var. Nə qədər olsun? ⚖️\n",
                f"Müştəri: {weight} kq olsun, amma yüngül olmasın, birdə çox dadlı olsun! 🍬🍫😋\n",
                f"Satıcı: Şirniyyat 🍪 hazırdır, qiyməti {total_price} manat. 💵🍫\n",
                f"Müştəri: Pulu, burdan çıxın. 💳😊\n",
                f"Satıcı: Buyurun, çeki təqdim edirəm. 🧾🍪\n"
            ],
            [
                f"Müştəri: Salam, bu gün şirniyyat 🎂 alıb özümü şənləndirmək istəyirəm. 🍰🎉\n",
                f"Satıcı: Salam! Gözəl fikirdir. Hansı şirniyyatdan 🍩 almaq istəyirsiniz? 🤩\n",
                f"Müştəri: Mənə {sweets} 🍪 lazımdır, amma mütləq dadı möhtəşəm olmalıdır! 😋🍬\n",
                f"Satıcı: Əlbəttə, {sweets} bizim ən sevilən şirniyyatımızdır. Hər zaman təzədir. 🧁💖\n",
                f"Müştəri: Məncə {weight} kq alınsa, kifayət edər. Həm də evdə bir az da ailə 👨‍👩‍👧‍👦 var. 🍪\n",
                f"Satıcı: Mükəmməl seçim! Bu qədər {weight} kq {sweets} 🍩 sizi heç yanıltmaz. Qiymət {total_price} manat. 💰🍫\n",
                f"Müştəri: Bu qiymətə razıyam, amma pulu yalnız ədalətli şəkildə verərəm! 🤝💵\n",
                f"Satıcı: Təbii ki! Bütün şirniyyatlarımız ədalətə uyğundur! Çekinizi təqdim edirəm. 🧾🍩\n",
                f"Müştəri: Çox sağ olun, şirniyyatla həyat çox dadlı olacaq. 😋🍰\n",
                f"Satıcı: Gələn dəfə də gözləyirik! 😊🎉\n"
            ]]

        # Random bir dialoq seçir.
        random_sweet_dialogue = random.choice(dialogue)

        return random_sweet_dialogue



    def cake_dialogue(self, *args):
        if len(args) != 3:
            return "Yalnız 3 argument göndərə bilərsiz.."

        cake, weight, total_price = args

        # Müştəri və satıcı arasında tort alarkən keçən dialoqlar:
        dialogue = [
            [
                f"Müştəri: Salam, bir tort 🍰 almaq istəyirəm.\n",
                f"Satıcı: Salam, hansı növ tort 🎂 istəyirsiniz?\n",
                f"Müştəri: {cake} 🍪 olsun.\n",  
                f"Satıcı: Bəs çəkisi nə qədər olsun? ⚖️\n",
                f"Müştəri: {weight} kq civarı olsun. 💪\n",  
                f"Satıcı: Tamam, buyurun tortunuz hazırdır, qiyməti {total_price} manat. 💵🍰\n",  
                f"Müştəri: Buyurun, pulu, burdan çıxa bilərsiniz. 💳😊\n",  
                f"Satıcı: Mağazamızdan istifadə etdiyiniz üçün təşəkkür edirik! Buyurun çeki. 🧾🎂\n" 
            ],
            [    
                f"Müştəri: Salam, bir tort 🍰 almaq istəyirəm, amma bir az fərqli 🤔 olsun.\n",
                f"Satıcı: Salam! Nə cür tort 🎂 istəyirsiniz? **Şokoladlı** 🍫, meyvəli 🍓, yoxsa bir az ekzotik 🌺 bir şey?\n",
                f"Müştəri: {cake} yaxşı olar, amma içində bol krem 🍫 olsun.\n", 
                f"Satıcı: Aha, kremli {cake}, çox yaxşı seçim! Çəkisi nə qədər olsun? ⚖️\n",
                f"Müştəri: {weight} kq olar, amma keyfiyyətli 🌟 olsun.\n", 
                f"Satıcı: Çox yaxşı, deməli, keyfiyyətli bir tort istəyirsiniz. Qiymət isə {total_price} manat. 💰🍰\n", 
                f"Müştəri: Hə, bu qiymət yaxşıdır, alıram. Pulu burada ödəyim. 💳😊\n", 
                f"Satıcı: Buyurun burada ödəyə bilərsiniz. 🧾💵\n", 
                f"Satıcı: Mağazamıza gəldiyiniz üçün təşəkkürlər! Ümid edirəm tortu çox bəyənərsiniz... 🍰🎉\n",
                f"Müştəri: Əlbəttə! Çox sağ olun, bir daha gələcəyəm! 😊🎂\n"
            ]]

        # Random dialoq seçir. 
        random_cake_dialogue = random.choice(dialogue)

        return random_cake_dialogue