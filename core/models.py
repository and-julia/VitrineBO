from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models


# PARÂMETROS DO SISTEMA #
# Estilos da loja
class EstiloLoja(models.Model):
    descEstiloLoja = models.CharField(max_length=50, blank=False, null=False, verbose_name='Estilo')
    
    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = 'Estilos da loja'
        

# Formas de pagamento
class PagamentoLoja(models.Model):
    descPagamentoLoja = models.CharField(max_length=50, blank=False, null=False, verbose_name='Forma de pagamento')
    
    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = 'Formas de pagamento'
        

# Formas de entrega
class EntregaLoja(models.Model):
    descEntregaLoja = models.CharField(max_length=50, blank=False, null=False, verbose_name='Forma de entrega')
    
    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = 'Formas de entrega'
 
       
# Tipo de produto
class TipoProduto(models.Model):
    descTipoProduto = models.CharField(max_length=50, blank=False, null=False, verbose_name='Tipo de produto')
    
    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = 'Tipos de produtos'


# Cor do produto
class CorProduto(models.Model):
    descCorProduto = models.CharField(max_length=50, blank=False, null=False, verbose_name='Cor')
    
    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = 'Cores'


# Status do produto
class StatusProduto(models.Model):
    descStatusProduto = models.CharField(max_length=50, blank=False, null=False, verbose_name='Status')
    
    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = 'Status'


# Gênero
class Genero(models.Model):
    descGenero = models.CharField(max_length=50, blank=False, null=False, verbose_name='Gênero')
    
    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = 'Gêneros'


# Tipo de perfil do colaborador
class TipoPerfilColaborador(models.Model):
    descTipoPerfil = models.CharField(max_length=50, blank=False, null=False, verbose_name='Tipo de perfil')
    
    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = 'Perfis dos colaboradores'


# Estados
class Estado(models.Model):
    nomeEstado = models.CharField(max_length=50, blank=False, null=False, verbose_name='Estado')
    
    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = 'Estados'


# Tipo de contato
class TipoContato(models.Model):
    descTipoContato = models.CharField(max_length=50, blank=False, null=False, verbose_name='Tipo de contato')
    
    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = 'Tipos de contato'





# USUÁRIOS #
class Usuario(models.Model):
    cpfUsuario = models.IntegerField(max_length=11, blank=False, null=False, verbose_name='CPF')
    nomeUsuario = models.CharField(max_length=100, blank=False, null=False, verbose_name='Nome')
    genero = models.ForeignKey(Genero, null=False, on_delete=models.PROTECT, verbose_name='Gênero')
    #avatarUsuario = models.ImageField(pasta de destino, blak e null, verbose)
    
    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = 'Usuários'





# LOJAS #
# Loja
class Loja(models.Model):
    cnpjLoja = models.IntegerField(max_length=14, blank=False, null=False, verbose_name='CNPJ')
    nomeFantasiaLoja = models.CharField(max_length=50, blank=False, null=False, verbose_name='Nome fantasia')
    razaoSocial = models.CharField(max_length=100, blank=False, null=False, verbose_name='Razão social')
    #logotipoLoja = models.ImageField(pasta de destino, blak e null, verbose)
        
    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = 'Lojas'
        
              
# Parceiros da loja (colaboradores)
class ParceiroLoja(models.Model):
    nomeParceiro = models.CharField(max_length=100, blank=False, null=False, verbose_name='Nome')
    perfilParceiro = models.ForeignKey(TipoPerfilColaborador, blank=False, null=False, verbose_name='Tipo de perfil')
    lojaParceiro = models.ForeignKey(Loja, blank=False, null=False)
    
    
    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = 'Parceiros'





# CADASTROS GERAIS #
# Contato
class Contato(models.Model):
    idTipoContato = models.ForeignKey(TipoContato, on_delete=models.PROTECT, verbose_name='Tipo de contato')
    contato = models.CharField(max_length=200, blank=False, null=False, verbose_name='Informação de contato')
    idUsuario = models.ForeignKey(Usuario, null=True, on_delete=models.PROTECT, verbose_name='Usuário')
    idLoja = models.ForeignKey(Loja, null=True, on_delete=models.PROTECT, verbose_name='Loja')


    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = 'Contatos'


# Endereço
class Endereco(models.Model):
    cep = models.IntegerField(max_length=8, blank=False, null=False, verbose_name='CEP')
    rua = models.CharField(max_length=100, blank=False, null=False, verbose_name='Rua')
    numero = models.IntegerField(max_length=5, blank=False, null=False, verbose_name='Número')
    complemento = models.CharField(max_length=20, blank=True, null=True, verbose_name='Complemento')
    bairro = models.CharField(max_length=50, blank=False, null=False, verbose_name='Bairro')
    cidade = models.CharField(max_length=50, blank=False, null=False, verbose_name='Cidade')
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, verbose_name='Estado')
    idUsuario = models.ForeignKey(Usuario, null=True, on_delete=models.PROTECT, verbose_name='Usuário')
    idLoja = models.ForeignKey(Loja, null=True, on_delete=models.PROTECT, verbose_name='Loja')


    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = 'Endereços'
        
        
# Acesso
class Acesso(models.Model):
    pass





# PRODUTOS
# Produtos
class Produto(models.Model):
    codigoInterno = models.CharField(max_length=50, blank=True, null=True, verbose_name='Código interno')
    tituloProduto = models.CharField(max_length=50, blank=True, null=True, verbose_name='Título do anúncio')
    descricaoProduto = models.CharField(max_length=500, blank=True, null=True, verbose_name='Descrição do produto')
    tipoProduto = models.ForeignKey(TipoProduto, null=False, on_delete=models.PROTECT, verbose_name='Tipo de produto')
    precoProduto = models.DecimalField(blank=True, null=True, verbose_name='Preço do produto')
    generoProdutos = models.ForeignKey(Genero, null=False, on_delete=models.PROTECT, verbose_name='Gênero')
    statusProduto =  models.ForeignKey(StatusProduto, null=False, on_delete=models.PROTECT, verbose_name='Status do produto')
    
    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = 'Produtos'


# Fotos
class Foto(models.Model):
    # fotoProduto = models.ImageField(diretorio, blank, null, verbose)
    idProduto = models.ForeignKey(Produto, on_delete=models.PROTECT, blank=False, null=False, verbose_name='Fotos do produto')

    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = 'Fotos'
    
    
# Perguntas
class Pergunta(models.Model):
    pass