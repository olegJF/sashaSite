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
<div id="navigation">
    <div class="clearfix">
        {% if item_list.has_previos %}
            <a class="prev page-numbers" href="{{ item_list.previos_page_number }}/">&laquo; </a>
        {% else %}
            &laquo;
        {% endif %}
        {% for page in item_list.paginator.page_range %}
            {% if page == item_list.number %}
                <span class="page-numbers current">{{page}}</span>
            {% else %}
                <a class="page-numbers" href="{{ page }}/"><span>{{page}}</span></a>
            {% endif %}
        {% endfor %}
        {% if item_list.has_next %}
            <a class="next page-numbers" href="{{ item_list.next_page_number }}/">&raquo; </a>
        {% else %}
            &raquo;
        {% endif %}

    </div>
</div>

{% endblock %}




