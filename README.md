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

<html>
<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>Surface Area</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <style type="text/css">
        body {
            background-color: grey;
        }
        .edge {
            width: 100%;
            max-width: 1440px;
            margin: 0 auto;
            padding-top: 20px;
            text-align: center;  /* Added text-align center */
        }
        .box {
            border: thick dashed sky yellow;
            width: 500px;
            min-height: 300px;
            font-size: 20px;
            background-color: light greenyellow;
            padding: 20px;
            box-sizing: border-box;
            display: inline-block;  /* Added display inline-block */
        }
        .formelt {
            color: goldenrod;
            text-align: center;
            margin-top: 7px;
            margin-bottom: 6px;
        }
        h1 {
            color: blue (255, 0, 119);
            text-align: center;
            padding-top: 20px;
            margin-bottom: 0;
        }
        .input-container {
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <h1>PHARSHEEN RAHUMAN M </h1>
    <h1>24006746</h1>
    <div class="edge">
        <div class="box">
            <h1>Surface Area of Right Cylinder</h1>
            <form method="POST">
                {% csrf_token %}
                <div class="input-container">
                    <div class="formelt">
                        Radius : <input type="text" name="radius" value="{{r}}"></input>(in m)
                    </div>
                </div>
                <div class="input-container">
                    <div class="formelt">
                        Height : <input type="text" name="height" value="{{h}}"></input>(in m)
                    </div>
                </div>
                <div class="formelt">
                    <input type="submit" value="Calculate"></input>
                </div>
                <div class="formelt">
                    Area : <input type="text" name="area" value="{{area}}"></input>m<sup>2</sup>
                </div>
            </form>
        </div>
    </div>
</body>
</html>


views.py

from django.shortcuts import render

def surfacearea(request):
    context = {}
    context['area'] = "0"
    context['r'] = "0"
    context['h'] = "0"

    if request.method == 'POST':
        print("POST method is used")
        r = request.POST.get('radius', '0')
        h = request.POST.get('height', '0')
        print('Radius=', r)
        print('Height=', h)

        try:
            r = float(r)
            h = float(h)
            area = (2 * 3.14159 * r * h) + (2 * 3.14159 * r * r)
            context['area'] = round(area, 2)
            context['r'] = str(r)
            context['h'] = str(h)
            print('Area=', area)
        except ValueError:
            print('Invalid input for radius or height.')

    return render(request, 'mine/min.html', context)

 urls.py

    from django.contrib import admin
from django.urls import path
from mine import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('surfacearea/', views.surfacearea, name="surfacearea"),
    path('', views.surfacearea, name="surfacearearoot")
]
```

## SERVER SIDE PROCESSING:
![alt text](<Screenshot (13).png>)

## HOMEPAGE:
![alt text](<Screenshot (12).png>)

## RESULT:
The program for performing server side processing is completed successfully.
