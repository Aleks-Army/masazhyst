(function(){
  var b=document.querySelector('.burger'),n=document.getElementById('nav');
  if(b&&n){b.addEventListener('click',function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o)});
    n.addEventListener('click',function(e){if(e.target.tagName==='A'&&!e.target.closest('.lang')){n.classList.remove('open');b.setAttribute('aria-expanded','false')}});}
  var f=document.getElementById('invite');
  if(f){f.addEventListener('submit',function(e){e.preventDefault();var ok=f.querySelector('.form-ok');ok.classList.add('show');ok.focus();});}
})();
