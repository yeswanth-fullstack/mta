from django.db import models

# Create your models here.


class TransactionSummary(models.Model):
    """Model to store transaction summary data for LIRR and MNR pages"""

    OPENCLOSE_CHOICES = [
        ("Open", "Open"),
        ("Closed", "Closed"),
    ]

    PAGE_CHOICES = [
        ("LIRR", "LIRR"),
        ("MNR", "MNR"),
    ]

    openclose = models.CharField(
        max_length=10, choices=OPENCLOSE_CHOICES, verbose_name="Status"
    )
    dept = models.CharField(max_length=100, verbose_name="Department")
    users = models.CharField(max_length=100, verbose_name="User")
    totalrefund = models.IntegerField(default=0, verbose_name="Total Refund")
    totalclaim = models.IntegerField(default=0, verbose_name="Total Claim")
    totalchargeback = models.IntegerField(default=0, verbose_name="Total Chargeback")
    totalpa61 = models.IntegerField(default=0, verbose_name="Total PA61")
    page = models.CharField(max_length=10, choices=PAGE_CHOICES, verbose_name="Page")

    # Additional fields for better data management
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Transaction Summary"
        verbose_name_plural = "Transaction Summaries"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["page", "dept"]),
            models.Index(fields=["openclose"]),
        ]

    def __str__(self):
        return f"{self.page} - {self.dept} - {self.users} ({self.openclose})"

    @property
    def total_transactions(self):
        """Calculate total of all transaction types"""
        return (
            self.totalrefund + self.totalclaim + self.totalchargeback + self.totalpa61
        )
