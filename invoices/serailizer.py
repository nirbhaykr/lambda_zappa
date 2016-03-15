from rest_framework import serializers
from invoices.models import Invoice, Transcation


class TransactionSerializer(serializers.ModelSerializer):

    """
    Purpose: A serializer that deals with Details instances and
    querysets.
    """

    class Meta(object):
        model = Transcation
#         fields = ('category',)
#         read_only_fields = ('entries',)
#         exclude = ('broken_url_flag',)


class InvoiceSerializer(serializers.ModelSerializer):
    transaction = TransactionSerializer(many=True,
                                    required=False, read_only=False)
#     transaction = serializers.SlugRelatedField(many=True, queryset=Transcation.objects.all(), read_only=False, slug_field='category')

    def create(self, validated_data):
        transaction_list = []
        if validated_data.get('transaction'):
            transaction_list = validated_data.pop('transaction')
        inv_obj = Invoice.objects.create(**validated_data)
        for tarnsaction_record in transaction_list:
            tran_obj = Transcation.objects.create(**tarnsaction_record)
            inv_obj.transaction.add(tran_obj)
        self.update_invoice(inv_obj)
        return inv_obj
    
    def update(self, instance, validated_data):
        transaction_list = []
        if validated_data.get('transaction'):
            transaction_list = validated_data.pop('transaction')
        inv_obj = instance
        inv_obj.transaction.all().delete()
        for tarnsaction_record in transaction_list:
            tran_obj = Transcation.objects.create(**tarnsaction_record)
            inv_obj.transaction.add(tran_obj)
        self.update_invoice(inv_obj)
        return inv_obj

    def update_invoice(self, instance):
        tran_data = instance.transaction.all()
        quantity = 0;
        amount = 0
        for tran_obj in tran_data:
            quantity += tran_obj.quantity
            amount = tran_obj.line_total
        instance.quantity = quantity
        instance.total_amount = amount
        instance.save()




    class Meta(object):
        model = Invoice
        fields = ('id','custumer', 'invoice_date', 'quantity', 'total_amount','transaction')
        depth = 1


