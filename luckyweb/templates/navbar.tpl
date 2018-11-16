<nav class="navbar navbar-expand-lg navbar-dark bg-dark" >
  <div class="container"> <a class="navbar-brand" href="{{ args.li_list[0].href }}">
      <i class="fa d-inline fa-lg fa-circle-o"></i>
      <b> {{ args.li_list[0].text }} </b>
    </a> <button class="navbar-toggler navbar-toggler-right border-0" type="button" data-toggle="collapse" data-target="#navbar11">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbar11">
      <ul class="navbar-nav mr-auto">
      {% for li in args.li_list[1:] %}
	    {% if li.get('active') %}
        <li class="nav-item active">
		{% else %}
        <li class="nav-item">
		{% endif %}
          <a href="{{ li.href }}" class="nav-link">{{ li.text }}</a>
        </li>
      {% endfor %}
      </ul>
      <ul class="navbar-nav ml-auto">
	  {% for ri in args.ri_list %}
	    {% if not ri.get('btn') %}
        <li class="nav-item"> <a class="nav-link" href="{{ ri.href }}">{{ ri.text }}</a> </li>
		{% else %}
	    <a class="btn btn-primary navbar-btn ml-md-2" href="{{ ri.href }}">{{ ri.text }}</a>
		{% endif %}
      {% endfor %}
      </ul>
    </div>
  </div>
</nav>
