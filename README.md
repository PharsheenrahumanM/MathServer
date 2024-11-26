# Ex.05 Design a Website for Server Side Processing
## Date:25/11/2024

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
min.html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Power Of A Lamp Filament In An Incandescent Bulb</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <style type="text/css">
        .edge {
            width: 1440px;
            margin-left: auto;
            margin-right: auto;
            padding-top: 300px;
            padding-left: 350px;
        }
        .box {
            display: block;
            border: thick dashed grey (8, 6, 17);
            width: 500px;
            min-height: 300px;
            font-size: 20px;
            background-color: blue (210, 210, 210);
        }
        .formelt {
            color: red (1, 18, 17);
            text-align: center;
            margin-top: 10px;
            margin-bottom: 7px;
        }
        h1 {
            text-align: center;
            padding-top: 25px;
        }
    </style>
</head>
<body>
    <div class="edge">
        <div class="box">
            <h1>Power Of A Lamp Filament In An Incandescent Bulb</h1>
            <h2>Name:Pharsheen Rahuman M Reg no:24006746</h2>
            <form method="POST">
                {% csrf_token %}
                <div class="formelt">
                    Intensity: <input type="text" name="intensity" value="{{ r }}"></input> (in amps)<br/>
                </div>
                <div class="formelt">
                    Resistance: <input type="text" name="resistance" value="{{ h }}"></input> (in ohms)<br/>
                </div>
                <div class="formelt">
                    <input type="submit" value="Calculate"></input><br/>
                </div>
                <div class="formelt">
                    Power: <input type="text" name="power" value="{{ power }}" readonly></input> watts<br/>
                </div>
            </form>
        </div>
    </div>
</body>
</html>


views.py
from django.shortcuts import render

def rectarea(request):
    context = {
        'power': "0",
        'r': "0",
        'h': "0"
    }
    if request.method == 'POST':
        print("POST method is used")
        r = request.POST.get('intensity', '0')
        h = request.POST.get('resistance', '0')
        
        try:
            intensity = float(r)
            resistance = float(h)
            
            power = (intensity ** 2) * resistance

            context['power'] = round(power, 2)
            context['r'] = r
            context['h'] = h
            print('intensity =', intensity)
            print('resistance =', resistance)
            print('power =', power)
        except ValueError:
            context['power'] = "Invalid input"
            print("Invalid input provided")
            
    return render(request, 'mine/min.html', context)

url.py
from django.contrib import admin 
from django.urls import path 
from mine import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('areaofrectangle/',views.rectarea,name="areaofrectangle"),
    path('',views.rectarea,name="areaofrectangleroot")
]

```

## SERVER SIDE PROCESSING:
![Screenshot 2024-11-26 173542](https://github.com/user-attachments/assets/df29d3e0-340d-4a4c-a427-55013fbb9e23)


## HOMEPAGE:
![Screenshot 2024-11-26 173419](https://github.com/user-attachments/assets/c76d5567-bd96-4a60-8461-a89af4f3d991)


## RESULT:
The program for performing server side processing is completed successfully.
