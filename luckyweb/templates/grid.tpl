<div class="py-{{ py }}">
  <div class="container-fluid">
    <div class="row">
      {% for i in cols_num|len|range %}
        <div class="col-sm-{{ cols_num[i] }}">
  		  {{ variable[i] }}
  	    </div>
  	  {% endfor %}
    </div>
  </div>
</div>
