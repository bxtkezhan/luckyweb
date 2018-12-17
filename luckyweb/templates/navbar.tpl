<nav class="navbar navbar-expand-lg {{ _class }}" >
  <div class="container"> <a class="navbar-brand" href="{{ left_items[0].href }}">
      <i class="fa d-inline fa-lg fa-circle-o"></i>
      <b> {{ left_items[0].text }} </b>
    </a> <button class="navbar-toggler navbar-toggler-right border-0" type="button" data-toggle="collapse" data-target="#navbar11">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbar11">
      <ul class="navbar-nav mr-auto">
      {% for item in left_items[1:] %}
	    {% if item.active %}
        <li class="nav-item active">
		{% else %}
        <li class="nav-item">
		{% endif %}
          <a href="{{ item.href }}" class="nav-link">{{ item.text }}</a>
        </li>
      {% endfor %}
      </ul>
      <ul class="navbar-nav ml-auto">
	  {% for item in right_items %}
	    {% if item.btn|not %}
        <li class="nav-item"> <a class="nav-link" href="{{ item.href }}">{{ item.text }}</a> </li>
		{% endif %}
      {% endfor %}
      </ul>
	  {% for item in right_items %}
	    {% if item.btn %}
      <a class="btn btn-primary navbar-btn ml-md-2" href="{{ item.href }}">{{ item.text }}</a>
		{% endif %}
      {% endfor %}
    </div>
  </div>
</nav>
