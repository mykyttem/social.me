from django.shortcuts import render, redirect


def main_page(request):
    if request.method == "POST":
        name = request.POST["name"]
        print(name)

        return redirect("profile")

    return render(request, 'main_page.html')


def profile(request):
    return render(request, 'profile.html')