/**
 * Created with JetBrains WebStorm.
 * User: kala
 * Date: 26.10.13
 * Time: 13:26
 * To change this template use File | Settings | File Templates.
 */


// name - description - koefficient - peoples
var categories = [
    ["Дети", "Дети скидываются меньше", 0.7, ["Коля"]],
    ["Общак", "Все, кто не попал в другие",  1, ["Вася", "Петя", "Коля"]],
    ["Алкоголики", "Все, кто алкоголики", 1, ["Вася"]]
];

// name - group - category
var persons = [
    ["Вася", "Ивановы", "Общак"],
    ["Петя", "Петровы", "Алкоголики"],
    ["Коля", "Петровы", "Дети"]
];
// name - date - users
var actions = [
    ["Зелёная",  "26.10.2013", ["Вася", "Петя"]],
    ["Новый год", "26.12.2013", ["Вася", "Петя", "Коля"]]
];
// name - cost - date - category - action
var purchases = [
    ["Шашлык", 1000, "14.10.2013", "Общак", 0],
    ["Угли", 100, "14.10.2013", "Общак",  0],
    ["Пиво", 2000, "14.10.2013", "Алкоголики", 0]
];

// Пробегаемся по людям
for(var i = 0; i < persons.length; ++i)
{
    console.log(persons[i][0] + " платит за:");
    // Пробегаемся по покупкам
    for(var j = 0; j < purchases.length; ++j)
    {
        // Если за покупку платят все ИЛИ какая-либо категория
        if((purchases[j][3] == "Общак") || (purchases[j][3] == persons[i][2]))
        {
            // Вычисляем общий коэффициент
            var koeff = 0;
            // Ищем коэффициент нашей категории
            var ourKoeff = 0;
            for(var k = 0; k < categories.length; ++k)
            {
                if(persons[i][2] == categories[k][0])
                    ourKoeff = categories[k][2];
            }
            //console.log("ourKoeff = " + ourKoeff);
            // Пробегаемся по людям, которые платят за этот предмет
            for(var k = 0; k < categories.length ; ++k)
            {
                // Если категория покупает предмет
                if((persons[k][2] == "Общак") || (persons[k][2] == purchases[j][3]))
                {
                    console.log("oldKoeff = "+categories[k][2]);
                    console.log("ourKoeff = "+ourKoeff);
                    console.log("categories[k][2] / ourKoeff = " + categories[k][2] / ourKoeff);
                    koeff += categories[k][2] / ourKoeff;
                }
            }
            var buy = purchases[j][1] / (koeff);
            console.log(" --> " + purchases[j][0] + " примерно " + buy + " денег");
        }
    }
}