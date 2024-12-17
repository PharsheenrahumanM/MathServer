from django.shortcuts import render

def power(request):
    context = {}
    context['power'] = "0"
    context['i'] = "0"
    context['r'] = "0"

    if request.method == 'POST':
        print("POST method is used")
        print('request.POST:', request.POST)
        
        # Get intensity and resistance from the form
        i = request.POST.get('intensity', '0')
        r = request.POST.get('resistance', '0')
        
        print('intensity =', i)
        print('resistance =', r)

        # Ensure that i and r are valid integers
        try:
            i = int(i)
            r = int(r)
        except ValueError:
            # If either i or r is not a valid number, set power to 0 and return an error message
            context['error'] = "Please enter valid numeric values for intensity and resistance."
            context['power'] = 0
            return render(request, 'mine/min.html', context)

        # Calculate power using the formula P = I^2 * R
        power = i * i * r
        context['power'] = power
        context['i'] = i
        context['r'] = r

        print('Power =', power)

    return render(request, 'mine/min.html', context)


   