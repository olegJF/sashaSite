{% extends 'index.html'%}

{% block title %}Home{% endblock %}

{% block content %}

<h2>Welcome to the Gallery!</h2>
<p>Here you'll find pictures of various items. Below are some highlighted
items; use the link at the bottom to see the full listing.</p>

<h3>Showcase</h3>
{% for item in item_list %}
     <div class="dirImgList">
        <div>
            <h4>{{ item.title }}</h4>
            <div class="dirImgWrapper">
            {% if item.photo_set.count %}
                <a href="album/{{ item.id }}/"  title="{{item.description}}">
                <img class="dirImgCntr" src="/{{ item.photo_set.all.0.image.thumb_url }}"  />
                </a>
            {% else %}
                <a href="album/{{ item.id }}/"  title="{{item.description}}">
                <img class="dirImgCntr" src="../../static/photos/no_img.thumb.jpg"  />
                </a>
            {% endif %}
            </div>
        </div>
     </div>
{% endfor %}
<div style="clear:both"></div>


{% endblock %}




