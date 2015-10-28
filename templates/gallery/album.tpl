{% extends "index.html" %}

{% block title %}{{object.title}}{% endblock %}

{% block content %}

<h2>{{ object.title }}</h2>
<p>{{ object.description }}</p>


<div id="imgGallery">
    <table class="output_photo" align="center" cellpadding="2" cellspacing="10">
        <tr>
            {% for photo in object.photo_set.all %}
            <td>
                <a href="{{ photo.get_absolute_url }}" rel="lightgallery[gallery]" title="{{ photo.title }}">
                    <img src="/{{ photo.image.thumb_url }}" alt=" " /><br>
                </a>
            </td>
            {% if more_one_line and forloop.counter in photos_rows%}
            </tr>
            <tr>
            {% endif %}
            {% endfor %}
        </tr>
    </table>
</div>
<div style="clear:both"></div>
<br>


<p><a href="{% url 'gallery' %}">&laquo; Назад в галлерею</a></p><br>

{% endblock %}

../../{{photo.image.url}}