// SEARCH

$(document).ready(function(){

    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');

    $(searchBtn).on('click', function(){
        searchForm.submit();
    });
});


// JANELA DE EXCLUSÃO COM JS

// <button class="btn-excluir" type="button" onclick="excluirCategoria('{{ categoria.id }}')">Excluir</button>

// function excluirCategoria(categoria_id) {
//     const url = "{% url 'excluir_categoria' 123 %}"
//     const confirm = window.confirm("Deseja excluir?")
//     if (confirm) {
//         window.location.assign(url.replace('123', categoria_id))
//     }
// }

