$(document).ready(function(){

    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');

    $(searchBtn).on('click', function(){
        searchForm.submit();
    });
});



function excluirCategoria(categoria_id) {
    const url = "{% url 'excluir_categoria' 123 %}"
    const confirm = window.confirm("Deseja excluir?")
    if (confirm) {
        window.location.assign(url.replace('123', categoria_id))
    }
}

<button class="btn-excluir" type="button" onclick="excluirCategoria('{{ categoria.id }}')">Excluir</button>

