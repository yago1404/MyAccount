# Refatoramento
<h3>Alterações</h3>
<ul>
<li>Foram criados dois novos métodos na classe MainMenu, dentro de outro metodo - login - para desagregar respossabilidades do mesmo, sem deixar com que outras classes e metodos da mesma classe tenham acesso a esses metodos aplicando um encapsulamento interno no próprio metodo, obedecendo as boas práticas do python disponiveis na documentação oficial. Esses dois novos metodos consistem na validação do login e senha fornecidos pelo cliente da aplicação</li>
<li>Foi retirado uma duplicação de código com um novo utilitário presente em until_functions/get_day.py ao adicionar a função getPaymentsDay que resolve a duplicidade que ocorria em duas outras classes que implementavam esse mesmo método da mesma forma</li>
<li>Foi retirado a quantidade de comentários presentes no arquivo main.py, onde as informações presentes foram colocadas em um arquivo de documentação license.py</li>
</ul>
