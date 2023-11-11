from django.shortcuts import render, redirect


def main_page(request):
    if request.method == "POST":
        name = request.POST["name"]
        selected_social_network = request.POST.getlist("social_media")

        # save session 
        request.session["name"] = name
        request.session["selected_social_network"] = selected_social_network

        # redirect on profile user 
        return redirect("profile")

    return render(request, 'main_page.html')


def profile(request):
    # get data from session
    name = request.session.get("name")
    selected_social_network = request.session.get("selected_social_network", [])

    print(selected_social_network)

    return render(request, 'profile.html', {'name': name, 'selected_social_network': selected_social_network})