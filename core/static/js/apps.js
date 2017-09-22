$(function(){


    // ajustar
   $('.documento').each(function(){
        var documento = ''
        if ($(this).is('th')){
            documento = $(this).text();
        }

        if ($(this).is('input')){
            documento = $(this).val();
        }

        doc = documento.replace(/[\.\-\/ ]+/g, '')
        if (doc.length == 14 ){

             $('.documento').mask('00.000.000/0000-00', {reverse: true});
        }else{
            $('.documento').mask('000.000.000-00', {reverse: true});
        }
   });

    function loadJobForm(){
         var btn = $(this);
        $.ajax({
            url: btn.attr('data-url'),
            type: 'GET',
            dataType: 'json',
            beforeSend: function(){
                $('#job-modal').modal('show');
            },
            success: function(data){
                $('#job-modal .modal-content').html(data.html_form);

                if(data.disable_all){
                    $('#job-modal input').attr('disabled','disabled');
                    $('#job-modal textarea').attr('disabled','disabled');
                    $('#job-modal select').attr('disabled','disabled');
                    $('#job-modal input[name=csrfmiddlewaretoken]').removeAttr('disabled');
                }
            }
        });
    };

    function saveJobForm(){
        var form =  $(this);
            $.ajax({
                url:  form.attr('action'),
                type: form.attr('method'),
                data: form.serialize(),
                dataType: 'json',

                success: function(data){
                    if(data.is_form_valid){

                        $('#cliente-table tbody').html(data.html_table);
                        $('.message').html(data.message)
                        $('#cliente-modal').modal('hide');

                    }else{
                        $('#cliente-modal .modal-content').html(data.html_form);
                        tipo = $('select').val()
                        if(tipo  == 2){
                            $('.documento').mask('000.000.000-00', {reverse: true});
                        }else{
                            $('.documento').mask('00.000.000/000-00', {reverse: true});
                        }
                    }
                }
        });
    return false;
    };


    function deleteJobForm(){
        var form =  $(this);
            $.ajax({
                url:  form.attr('action'),
                type: form.attr('method'),
                data: form.serialize(),
                dataType: 'json',
                beforeSend:function(){

                    var x = confirm('Você realmente deseja desativar esse cliente ?')
                    if (x == false){
                        return false;
                    }

                },
                success: function(data){
                    if(data.is_form_valid){

                        $('#cliente-table tbody').html(data.html_table);
                        $('.message').html(data.message)
                        $('#cliente-modal').modal('hide');

                    }else{
                        $('#cliente-modal .modal-content').html(data.html_form);
                        tipo = $('select').val()
                        if(tipo  == 2){
                            $('.documento').mask('000.000.000-00', {reverse: true});
                        }else{
                            $('.documento').mask('00.000.000/000-00', {reverse: true});
                        }
                    }
                }
        });
    return false;
    };

    // save job form
    $('.js-open-form-job').click(loadJobForm);
    $('#job-modal').on('submit', '.js-save-job-form', saveJobForm);




    // company  methods

    function loadCompanyForm(){
        var btn =  $(this);
        $.ajax({
            url:        btn.attr('data-url'),
            type:       'GET',
            dataType:   'json',

            beforeSend: function(){
                $('#company-modal').modal('show');
            },
            success: function(data){
                $('#company-modal .modal-content').html(data.html_form);
                if(data.disable_all){

                    $('input').attr('disabled', 'disabled')
                    $('textarea').attr('disabled', 'disabled')
                    $('select').attr('disabled', 'disabled')
                    $('#modal .btn-primary').attr('disabled', 'disabled')
                    $('input[name=csrfmiddlewaretoken]').removeAttr('disabled')


                }
            }
        });
    };

    function saveCompanyForm(){
        var form = $(this);
        $.ajax({
            dataType: 'json',
            url:  form.attr('action'),
            type: form.attr('method'),
            data: form.serialize(),

            success: function(data){
                if(data.is_form_valid){
                    $('#table-company tbody').html(data.html_table);
//                    $('#client-form').html(data.html_form);
                    $('.messages').html(data.message);
                    $('#company-modal').modal('hide');


                }else{

                    $('#company-modal .modal-content').html(data.html_form);
                }
            }
        });
    return false;
    };

    function deleteCompanyForm(){
        var form = $(this);
        $.ajax({

            dataType:'json',
            data: form.serialize(),
            url: form.attr('action'),
            type: 'post',

            beforeSend: function(){
                var x = confirm('Voce realmente deseja Desativar esse cliente ?')
                if(x == false){
                    return false;
                }
            },
            success: function(data){

                $('#contact-table tbody').html(data.html_table);
                $('.pagination').html(data.html_pagination)
                $('#modal').modal('hide');
                $('.messages').html(data.message);

            }

        });
     return false;
    };

    // save company
    $('.js-open-company-form').click(loadCompanyForm);
    $('#company-modal').on('submit', '.js-save-company-form', saveCompanyForm);

    // update company
    $('#company-table').on('click', '.js-open-company-form-update', loadCompanyForm);
    $('#company-modal').on('submit', '.js-company-form-update', saveCompanyForm);

    // delete company
    $('#comapny-table').on('click' , '.js-open-company-form-delete', loadCompanyForm);
    $('#comapny-modal').on('submit', '.js-company-form-delete', deleteCompanyForm);


    // method end
    function loadEnderecoForm(){
        btn = $(this);

        $.ajax({

            url: btn.attr('data-url'),
            type: 'get',
            dataType: 'json',

            beforeSend: function(){
                $('#modal').modal('show');
            },
            success: function(data){
                $('#modal .modal-content').html(data.html_form);

                if(data.disable_all){

                    $.each($('#modal input') , function(){
                        $("#modal input").attr('disabled','disabled');
                        $("#modal textarea").attr('disabled','disabled');
                        $("#modal select").attr('disabled','disabled');
                        $('input[name=csrfmiddlewaretoken]').removeAttr('disabled');
                    });

                }else{
                    $.each($('#modal input') , function(){
                        $("#modal input").removeAttr('disabled');
                    });


                }

            }

        });

    };

    function saveEndForm(){

        // liberar para que o cliente seja enviado no form.
        $("#id_cliente").removeAttr('disabled');
        var form = $(this);
        $.ajax({

            dataType: 'json',
            url: form.attr('action'),
            data: form.serialize(),
            type: form.attr('method'),

            success: function(data){

                if(data.is_form_valid){

                    $('.messages').html(data.message)
                    $('#address-table tbody').html(data.html_table);
                    $('.pagination_end').html(data.html_pagination);
                    $('#modal').modal('hide');

                }else{

                    $('#modal .modal-content').html(data.html_form);

                }

            }

        });
    return false;
    };

    //  abre o formulario de cadastro do endereço de cliente
    $('.js-open-end-form').click(loadEnderecoForm );
    $('#modal').on('submit', '.js-save-end-form', saveEndForm);

    $('#address-table').on('click', '.js-open-end-form-update' , loadEnderecoForm );
    $('#modal').on('submit' , '.js-update-end-form', saveEndForm)

    $('#address-table').on('click', '.js-open-end-form-delete' , loadEnderecoForm );
    $('#modal').on('submit' , '.js-delete-end-form', function(){

        var form  = $(this);
        $.ajax({

            dataType: 'json',
            data: form.serialize(),
            url: form.attr('action'),
            type: form.attr('method'),

            beforeSend: function(){
                var ask =  confirm('Deseja realmente desativar esse formulario ?')
                if(ask  == false){
                    return false;
                }

            },
            success: function(data){

                $('.messages').html(data.message)
                $('#address-table tbody').html(data.html_table);
                $('.pagination_end').html(data.html_pagination);

                $('#modal').modal('hide');
            }

        });
      return false;
      });



    //  busca o cep pelo viaCep
    $('#modal').on('click', '.search_cep' , function(){

        var cep =  $('.input_cep').val();
        cep  = cep.replace('-', '')
        var validacep = /^[0-9]{8}$/;


       // para ceps validos
        if(validacep.test(cep)){

            $.getJSON("http://viacep.com.br/ws/"+ cep +"/json/?callback=?", function(dados) {
                if (!("erro" in dados)) {

                    $('#id_cep').mask('00000-000');

                    // update endereco
                    $('#id_endereco').val(dados.logradouro);
                    $('#id_bairro').val(dados.bairro);
                    $('#id_cidade').val(dados.localidade);
                    $('#id_uf').val(dados.uf);
                }
                else {
                    //CEP pesquisado não foi encontrado.
                    alert("CEP não encontrado.");
                }
            }); // get json

        }// valida cep
        else{

            alert('CEP invalido. \nverifique o campo CEP.')
        }

    });

    // limpa o modal de endereço
    $('#modal').on('click', '.form_cleaned' , function(){
             $.each($('#modal input'),function(){
                $(this).val('');
            });

            $('textarea').val('');

    });


    $('#modal-group').on('shown.bs.modal', function(){
        $('.modal .modal-body').css('overflow-y','auto');
        $('.modal .modal-body').css('height' , $(window).height() * 0.7 );
    });

    $('#modal-group').on('hidden.bs.modal', function () {
        $('#modal-product').modal('show');

        $.ajax({
            url: 'api/product/group/list/',
            dataType: 'json',

            success: function(data){

                 var json_obj = $.parseJSON(data.groups);
                 if(json_obj ){
                    $('select[name=group] option').remove();
                   // <option value="" selected="selected">---------</option>
                    $('select[name=group]').append($('<option>').text('---------').
                    attr('selected','selected').attr('value',''));
                 }
                 $.each(json_obj, function(key, obj){
                      $('select[name=group]').append($('<option>').text(obj.fields.group).attr('value', obj.pk));

                 });

            }

        });
    });



});