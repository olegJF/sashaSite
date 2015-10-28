{% extends "index.html" %}

{% block title %}{{ object.name }}{% endblock %}

{% block content %}

<p><a href="{% url item_list %}">&laquo; Back to full listing</a></p>

<h2>{{ object.name }}</h2>
<p>{{ object.description }}</p>

<h3>Photos</h3>
<table>
    <tr>
        <th>Title</th>
        <th>Thumbnail</th>
        <th>Caption</th>
    </tr>
    {% for photo in object.photo_set.all %}
    <tr>
        <td><i>{{ photo.title }}</i></td>
        <td>
            <img src="{{ photo.image.thumb_url }}" />

        </td>
        <td>{{ photo.caption }}</td>
    </tr>
    {% endfor %}
</table>

{% endblock %}
