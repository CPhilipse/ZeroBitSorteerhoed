from django.shortcuts import render

def show_results(request, username):
    data = request.POST
    f = open(f'results/results{username}.txt', 'r')

    for i in f:
        fields = i.split(":")
        bdam = fields[0]
        fict = fields[1]
        iat = fields[2]
        se = fields[3]

        list = {"bdam": fields[0], "fict": fields[1], "iat": fields[2], "se": fields[3]}

        output = max(list)

        uitslag = [
            {
                'uitkomst': output
            }
        ]

        if "bdam" in output:
            print("BDAM is het resultaat")
        elif "fict" in output:
            print("FICT is het resultaat")
        elif "iat" in output:
            print("IAT is het resultaat")
        else:
            print("SE is het resultaat")

    f.close()

    context = {
        'uitslag': uitslag
    }
    return render(request, 'index.html', context)



