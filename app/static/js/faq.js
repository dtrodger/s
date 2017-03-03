$(document).ready(function() {
  $('button').on('click', function() {
    $(this).next('.answer').slideToggle();
    $(this).toggleClass('opened');
    $(this).find('i').toggleClass('rotate-90');
  });
});